#!/usr/bin/env python3
"""Reconstruye el diccionario desde el DDL, aplicando cambios en orden."""
from collections import OrderedDict
from pathlib import Path
import re
import os
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
MIG_DIR = BASE_DIR.parent.parent / 'db' / 'migrations'
OUTPUT_PATH = BASE_DIR / 'appendices' / 'b-anexo.md'
ENGINE = BASE_DIR.parent / 'docskill'
sys.path.insert(0, str(ENGINE))
os.environ.setdefault('DOCSKILL_PANDOC', str(ENGINE / '.tools/pandoc/bin/pandoc'))
from docskill import DocSkillProject

IDENT = r'(?:"(?:[^"]|"")+"|[A-Za-z_][A-Za-z0-9_$]*)'
TABLE_RE = re.compile(rf'^(?:ONLY\s+)?(?:(?:public)\.)?({IDENT})$', re.I)
STOP_TYPE = re.compile(r'\s+(?=(?:NOT\s+NULL|NULL\b|DEFAULT\b|REFERENCES\b|PRIMARY\s+KEY|UNIQUE\b|CHECK\s*\(|CONSTRAINT\b|COLLATE\b|GENERATED\b|IDENTITY\b))', re.I)

def ident(value):
    return value.strip().strip('"').replace('""', '"').lower()

def strip_comments(sql):
    """Quita comentarios SQL sin tocar cadenas, identificadores ni cuerpos dollar-quoted."""
    out, i, n, state, dollar = [], 0, len(sql), 'normal', None
    while i < n:
        if state == 'normal':
            if sql.startswith('--', i):
                state = 'line'; i += 2; continue
            if sql.startswith('/*', i):
                state = 'block'; i += 2; continue
            if sql[i] == "'": state = 'single'
            elif sql[i] == '"': state = 'double'
            elif sql[i] == '$':
                m = re.match(r'\$[A-Za-z_0-9]*\$', sql[i:])
                if m: dollar = m.group(); state = 'dollar'; out.append(dollar); i += len(dollar); continue
            out.append(sql[i]); i += 1
        elif state == 'line':
            if sql[i] == '\n': out.append('\n'); state = 'normal'
            i += 1
        elif state == 'block':
            if sql.startswith('*/', i): state = 'normal'; i += 2
            else:
                if sql[i] == '\n': out.append('\n')
                i += 1
        elif state in ('single', 'double'):
            quote = "'" if state == 'single' else '"'
            out.append(sql[i])
            if sql[i] == quote:
                if i + 1 < n and sql[i + 1] == quote: out.append(sql[i + 1]); i += 2; continue
                state = 'normal'
            elif sql[i] == '\\' and state == 'single' and i + 1 < n:
                out.append(sql[i + 1]); i += 2; continue
            i += 1
        else:
            if sql.startswith(dollar, i): out.append(dollar); i += len(dollar); state = 'normal'; dollar = None
            else: out.append(sql[i]); i += 1
    return ''.join(out)

def split_top(text, delimiter=','):
    parts, start, depth, i, quote, dollar = [], 0, 0, 0, None, None
    while i < len(text):
        if dollar:
            if text.startswith(dollar, i): i += len(dollar); dollar = None; continue
            i += 1; continue
        ch = text[i]
        if quote:
            if ch == quote:
                if i + 1 < len(text) and text[i + 1] == quote: i += 2; continue
                quote = None
        elif ch in ('"', "'"): quote = ch
        elif ch == '$':
            dm = re.match(r'\$[A-Za-z_0-9]*\$', text[i:])
            if dm: dollar = dm.group(); i += len(dollar); continue
        elif ch == '(': depth += 1
        elif ch == ')': depth -= 1
        elif depth == 0 and text.startswith(delimiter, i):
            parts.append(text[start:i].strip()); i += len(delimiter); start = i; continue
        i += 1
    parts.append(text[start:].strip())
    return [p for p in parts if p]

def statements(sql):
    # Semicolons inside quoted strings or dollar-quoted procedural bodies are ignored.
    return split_top(strip_comments(sql), ';')

def matching_paren(text, open_at):
    depth, quote, i = 0, None, open_at
    while i < len(text):
        ch = text[i]
        if quote:
            if ch == quote:
                if i + 1 < len(text) and text[i + 1] == quote: i += 2; continue
                quote = None
        elif ch in ('"', "'"): quote = ch
        elif ch == '(': depth += 1
        elif ch == ')':
            depth -= 1
            if depth == 0: return i
        i += 1
    raise ValueError('Paréntesis DDL sin cierre')

def split_type_rest(definition):
    m = re.match(rf'^\s*({IDENT})\s+(.+?)\s*$', definition, re.S)
    if not m: raise ValueError(f'Definición de columna no reconocida: {definition[:100]}')
    name, rest = ident(m.group(1)), m.group(2).strip()
    depth, quote, stop = 0, None, None
    for match in STOP_TYPE.finditer(rest):
        at = match.start()
        # A keyword inside a type modifier such as timestamp with time zone is not a stop.
        prefix = rest[:at]
        if prefix.count('(') != prefix.count(')'): continue
        stop = at; break
    typ = (rest[:stop] if stop is not None else rest).strip()
    attrs = (rest[stop:] if stop is not None else '').strip()
    return name, typ, attrs

def constraint_name(sql, index):
    m = re.match(rf'^CONSTRAINT\s+({IDENT})', sql, re.I)
    if m: return ident(m.group(1))
    if re.match(r'^PRIMARY\s+KEY', sql, re.I): return 'pkey'
    return f'anon_{index}'

def parse_constraint(sql, index):
    return {'name': constraint_name(sql, index), 'sql': ' '.join(sql.split())}

def columns_list(value):
    return [ident(x.split()[0]) for x in split_top(value)]

def add_inline_constraints(table, column, attrs):
    # PostgreSQL's default names let later DROP CONSTRAINT remove inline rules.
    table_name = table['name']
    explicit = re.search(rf'\bCONSTRAINT\s+({IDENT})', attrs, re.I)
    if re.search(r'\bPRIMARY\s+KEY\b', attrs, re.I):
        table['columns'][column]['nullable'] = False
    if re.search(r'\bUNIQUE\b', attrs, re.I): table['uniques'].append((column,))
    fk = re.search(rf'\bREFERENCES\s+(?:(?:public)\.)?({IDENT})(?:\s*\(([^)]*)\))?', attrs, re.I)
    if fk:
        targets = tuple(columns_list(fk.group(2))) if fk.group(2) else ()
        table['fks'].append(((column,), ident(fk.group(1)), targets, f'inline:{column}'))
    ck = re.search(r'\bCHECK\s*\(', attrs, re.I)
    if ck:
        end = matching_paren(attrs, attrs.index('(', ck.start()))
        cname = ident(explicit.group(1)) if explicit else f'{table_name}_{column}_check'
        start = explicit.start() if explicit else ck.start()
        table['constraints'][cname] = {'name': cname, 'sql': attrs[start:end+1], 'column': column}

def parse_constraint_semantics(table, cons):
    sql = cons['sql']
    m = re.search(r'\bPRIMARY\s+KEY\s*\((.*?)\)', sql, re.I)
    if m:
        cols = tuple(columns_list(m.group(1))); table['pks'].append(cols)
        for c in cols:
            if c in table['columns']: table['columns'][c]['nullable'] = False
    m = re.search(rf'\bFOREIGN\s+KEY\s*\((.*?)\)\s*REFERENCES\s+(?:(?:public)\.)?({IDENT})(?:\s*\((.*?)\))?', sql, re.I)
    if m:
        src = columns_list(m.group(1)); dest = columns_list(m.group(3)) if m.group(3) else []
        if dest and len(src) != len(dest): raise ValueError(f'FK con cardinalidad desigual: {sql}')
        table['fks'].append((tuple(src), ident(m.group(2)), tuple(dest), cons['name']))
    m = re.search(r'\bUNIQUE\s*\((.*?)\)', sql, re.I)
    if m: table['uniques'].append(tuple(columns_list(m.group(1))))

def new_table(version, name=''):
    return {'created': version, 'name':name, 'columns': OrderedDict(), 'constraints': OrderedDict(), 'pks': [], 'fks': [], 'uniques': [], 'excludes': [], 'dropped_constraints':set()}

def parse_create(statement, version, tables):
    m = re.match(rf'^CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?(?:(?:public)\.)?({IDENT})\s*\(', statement, re.I | re.S)
    if not m: return
    name = ident(m.group(1)); open_at = m.end()-1; close_at = matching_paren(statement, open_at)
    table = tables.setdefault(name, new_table(version, name))
    for part in split_top(statement[open_at+1:close_at]):
        if re.match(r'^(?:CONSTRAINT\b|PRIMARY\s+KEY\b|FOREIGN\s+KEY\b|UNIQUE\b|CHECK\s*\(|EXCLUDE\b)', part, re.I):
            cons = parse_constraint(part, len(table['constraints'])+1); table['constraints'][cons['name']] = cons
        else:
            col, typ, attrs = split_type_rest(part)
            table['columns'][col] = {'type': typ, 'nullable': not bool(re.search(r'\bNOT\s+NULL\b|\bPRIMARY\s+KEY\b', attrs, re.I)), 'default': default_value(attrs), 'attrs': attrs}
            add_inline_constraints(table, col, attrs)

def default_value(attrs):
    m = re.search(r'\bDEFAULT\s+(.+?)(?=\s+(?:NOT\s+NULL|NULL\b|REFERENCES\b|PRIMARY\s+KEY|UNIQUE\b|CHECK\s*\(|CONSTRAINT\b|COLLATE\b|GENERATED\b|IDENTITY\b)|$)', attrs, re.I)
    return m.group(1).strip() if m else None

def parse_alter(statement, tables):
    m = re.match(rf'^ALTER\s+TABLE\s+(?:IF\s+EXISTS\s+)?(?:(?:ONLY)\s+)?(?:(?:public)\.)?({IDENT})\s+(.+)$', statement, re.I | re.S)
    if not m: return
    name, actions = ident(m.group(1)), split_top(m.group(2))
    if name not in tables: return
    table = tables[name]
    for action in actions:
        if re.match(r'^ADD\s+(?:COLUMN\s+)?', action, re.I):
            definition = re.sub(r'^ADD\s+(?:COLUMN\s+)?(?:IF\s+NOT\s+EXISTS\s+)?', '', action, flags=re.I)
            if re.match(r'^(?:CONSTRAINT\b|PRIMARY\s+KEY\b|FOREIGN\s+KEY\b|UNIQUE\b|CHECK\s*\(|EXCLUDE\b)', definition, re.I):
                cons = parse_constraint(definition, len(table['constraints'])+1); table['constraints'][cons['name']] = cons
                continue
            col, typ, attrs = split_type_rest(definition)
            if col in table['columns'] and re.search(r'\bIF\s+NOT\s+EXISTS\b', action, re.I): continue
            table['columns'][col] = {'type': typ, 'nullable': not bool(re.search(r'\bNOT\s+NULL\b|\bPRIMARY\s+KEY\b', attrs, re.I)), 'default': default_value(attrs), 'attrs': attrs}
            add_inline_constraints(table, col, attrs)
        elif re.match(r'^DROP\s+COLUMN\b', action, re.I):
            col = ident(re.sub(r'^DROP\s+COLUMN\s+(?:IF\s+EXISTS\s+)?', '', action, flags=re.I).split()[0])
            table['columns'].pop(col, None)
        elif re.match(r'^DROP\s+CONSTRAINT\b', action, re.I):
            cname = ident(re.sub(r'^DROP\s+CONSTRAINT\s+(?:IF\s+EXISTS\s+)?', '', action, flags=re.I).split()[0])
            table['constraints'].pop(cname, None)
            table['dropped_constraints'].add(cname)
        elif re.match(r'^ALTER\s+COLUMN\b', action, re.I):
            am = re.match(rf'^ALTER\s+COLUMN\s+({IDENT})\s+(.+)$', action, re.I | re.S)
            if not am: continue
            col, op = ident(am.group(1)), am.group(2).strip()
            if col not in table['columns']: continue
            c = table['columns'][col]
            if re.match(r'^DROP\s+NOT\s+NULL\b', op, re.I): c['nullable'] = True
            elif re.match(r'^SET\s+NOT\s+NULL\b', op, re.I): c['nullable'] = False
            elif re.match(r'^TYPE\b|^SET\s+DATA\s+TYPE\b', op, re.I):
                typ = re.sub(r'^(?:TYPE|SET\s+DATA\s+TYPE)\s+', '', op, flags=re.I)
                typ = re.split(r'\s+USING\s+', typ, maxsplit=1, flags=re.I)[0].strip()
                c['type'] = typ
            elif re.match(r'^SET\s+DEFAULT\b', op, re.I): c['default'] = re.sub(r'^SET\s+DEFAULT\s+', '', op, flags=re.I).strip()
            elif re.match(r'^DROP\s+DEFAULT\b', op, re.I): c['default'] = None
        elif re.match(r'^RENAME\s+COLUMN\b', action, re.I):
            rm = re.match(rf'^RENAME\s+COLUMN\s+({IDENT})\s+TO\s+({IDENT})$', action, re.I)
            if rm:
                old, new = ident(rm.group(1)), ident(rm.group(2))
                if old in table['columns']:
                    table['columns'][new] = table['columns'].pop(old)

def domain(name):
    for words, label in [(['usuario','sesion','token','perfil','registro','auth','credencial','bloqueo_cuenta'], 'Identidad, autenticación y cuentas'), (['verificacion','kyc','documento_identidad'], 'Verificación KYC/KYB'), (['espacio','caracteristica','regla_espacio','foto','multimedia','categoria'], 'Espacios, publicaciones y catálogo'), (['reserva','cotizacion','ocupacion','horario','tarifa','bloqueo_agenda'], 'Reservas, disponibilidad y agendas'), (['pago','transaccion','escrow','reembolso','liquidacion','cobro','adquirente'], 'Transacciones financieras'), (['contrato','firma','clausula','folio'], 'Contratación digital'), (['inspeccion','checkin','checkout','evidencia','disputa','reclamo','dano'], 'Operaciones en recinto y disputas')]:
        if any(x in name for x in words): return label
    return 'Gobernanza, privacidad y administración'

def description(name, info):
    if name == 'id': return 'Identificador registrado en el esquema; la clave se indica en restricciones.'
    if name in ('creado_en','creada_en','created_at'): return 'Marca temporal de creación del registro.'
    if name in ('actualizado_en','actualizada_en','updated_at'): return 'Marca temporal de actualización del registro.'
    if name == 'intervalo': return 'Intervalo temporal; consulte el tipo y las restricciones declaradas.'
    if name in ('tarifa_version', 'precio_version', 'version_tarifa'): return 'Versión asociada a la tarifa; no representa por sí misma un monto.'
    if info['type'].lower().startswith(('numeric','decimal','money')) and any(x in name for x in ('monto','precio','importe','comision','deposito')): return 'Valor numérico de la magnitud indicada por el nombre de la columna.'
    return f'Atributo `{name}`; el nombre y tipo se conservan según el DDL.'

def render(tables):
    domains = OrderedDict()
    for name in sorted(tables): domains.setdefault(domain(name), []).append(name)
    out = ['# Anexo B — Diccionario de Datos del Esquema Físico PostgreSQL', '', 'Este catálogo se reconstruye aplicando en orden las migraciones SQL estructurales disponibles. Las claves y nulabilidades corresponden al estado resultante de esas definiciones; no implica que se haya consultado una base persistente.', '', f'El inventario contiene **{len(tables)} tablas físicas**. Las relaciones foráneas indican las columnas origen y destino declaradas en `REFERENCES`; las claves compuestas se identifican como conjuntos.', '']
    idx = 0
    for label, names in domains.items():
        out += [f'## Dominio: {label}', '']
        for name in names:
            idx += 1; table = tables[name]
            out += [f'### B.{idx:03d} Tabla `public.{name}`', f'- **Migración de creación:** `V{table["created"]:06d}`', f'- **Atributos:** {len(table["columns"])}', '', '| Columna | Tipo | Restricción y nulabilidad | Descripción basada en DDL |', '|---|---|---|---|']
            pk_sets = [x for x in table['pks'] if len(x) > 1]
            unique_sets = [x for x in table['uniques'] if len(x) > 1]
            for col, info in table['columns'].items():
                tags = []
                for pk in table['pks']:
                    if col in pk: tags.append('PK' + (f' compuesta ({", ".join(pk)})' if len(pk)>1 else ''))
                for unique in table['uniques']:
                    if col in unique: tags.append('UQ' + (f' compuesta ({", ".join(unique)})' if len(unique)>1 else ''))
                for src_cols, dst_table, dst_cols, constraint in table['fks']:
                    if col in src_cols:
                        if not dst_cols and dst_table in tables:
                            target = tables[dst_table]
                            candidates = [k for k in target['pks'] + target['uniques'] if len(k) == len(src_cols)]
                            dst_cols = tuple(candidates[0]) if candidates else ()
                        pairs = ', '.join(f'{a}→{b}' for a, b in zip(src_cols, dst_cols)) if len(src_cols) == len(dst_cols) and dst_cols else ', '.join(src_cols)
                        tags.append(f'FK → `public.{dst_table}({pairs})`' + (f' [{constraint}]' if not constraint.startswith('inline:') else ''))
                null = 'NOT NULL' if not info['nullable'] or any(col in p for p in table['pks']) else 'NULL permitido'
                if info['default'] is not None: tags.append(f'DEFAULT `{info["default"]}`')
                restriction = '; '.join(tags + [null])
                out.append(f'| `{col}` | `{info["type"].replace("|", "\\|")}` | {restriction} | {description(col, info)} |')
            out.append('')
            if table['constraints']:
                out += ['**Restricciones DDL vigentes:**', '']
                for con in table['constraints'].values(): out.append('- `' + con['sql'].replace('`','\\`') + '`')
                out.append('')
            out.append('')
    return '\n'.join(out)

def validate_inventory(tables, markdown):
    errors = []
    if len(tables) != 110: errors.append(f'conteo de tablas distinto al inventario esperado (110): {len(tables)}')
    for tname, table in tables.items():
        for cols in table['pks']:
            for col in cols:
                if col not in table['columns']: errors.append(f'PK referencia columna inexistente: {tname}.{col}')
                elif table['columns'][col]['nullable']: errors.append(f'PK nullable en extracción: {tname}.{col}')
        for src_cols, dst, dst_cols, constraint in table['fks']:
            if dst not in tables: errors.append(f'FK apunta a tabla inexistente: {tname} → {dst} ({constraint})'); continue
            if any(c not in table['columns'] for c in src_cols): errors.append(f'FK origen inexistente: {tname}.{src_cols} ({constraint})')
            if not dst_cols:
                candidates = [key for key in tables[dst]['pks'] + tables[dst]['uniques'] if len(key) == len(src_cols)]
                if not candidates: errors.append(f'FK sin columnas destino explícitas ni clave candidata: {tname}.{src_cols} → {dst} ({constraint})')
            elif len(dst_cols) != len(src_cols): errors.append(f'FK con pares incompletos: {tname}.{src_cols} → {dst}.{dst_cols} ({constraint})')
            elif any(c not in tables[dst]['columns'] for c in dst_cols): errors.append(f'FK destino inexistente: {tname}.{src_cols} → {dst}.{dst_cols} ({constraint})')
        for cons in table['constraints'].values():
            if len(cons['sql']) < 5: errors.append(f'Restricción vacía: {tname}.{cons["name"]}')
    # Contrastes puntuales citados por la revisión y controles de integridad de salida.
    for tname, col in [('bloqueo_cuenta_administrativo_local','bloqueada_por'), ('bloqueo_cuenta_historial_local','actor_id')]:
        if tname not in tables or col not in tables[tname]['columns'] or not tables[tname]['columns'][col]['nullable']:
            errors.append(f'V000042 no refleja nulabilidad final en {tname}.{col}')
    checks = [c for c in tables.get('verificacion', {}).get('constraints', {}).values() if c['name'] == 'verificacion_estado_ck']
    if len(checks) != 1 or "'retirada_privacidad'" not in checks[0]['sql']:
        errors.append('verificacion_estado_ck no tiene exactamente su definición final esperada')
    if 'PK (NULL)' in markdown or re.search(r'\| `tarifa_version` \|[^\n]*Monto monetario', markdown, re.I):
        errors.append('hay nulabilidad PK inválida o tarifa_version descrita como monto')
    if re.search(r'\| `propietario_id` \|[^\n]*FK → `public\.propietario\(', markdown):
        errors.append('se infiere entidad FK desde el sufijo propietario_id')
    if errors: raise ValueError('Falló auditoría del diccionario:\n- ' + '\n- '.join(errors))

def build_anexo_b():
    tables = OrderedDict()
    files = sorted(MIG_DIR.glob('V*.sql'))
    for path in files:
        vm = re.match(r'V(\d+)__', path.name)
        if not vm: continue
        version = int(vm.group(1))
        for stmt in statements(path.read_text(encoding='utf-8')):
            if re.match(r'^CREATE\s+TABLE\b', stmt, re.I): parse_create(stmt, version, tables)
            elif re.match(r'^ALTER\s+TABLE\b', stmt, re.I): parse_alter(stmt, tables)
    for table in tables.values():
        # Rebuild column-level keys from surviving columns and active constraint names;
        # this discards inline keys removed by a later DROP COLUMN/CONSTRAINT.
        table['pks'], table['fks'], table['uniques'] = [], [], []
        for col, info in table['columns'].items():
            attrs = info['attrs']; explicit = re.search(rf'\bCONSTRAINT\s+({IDENT})', attrs, re.I)
            if re.search(r'\bPRIMARY\s+KEY\b', attrs, re.I):
                cname = ident(explicit.group(1)) if explicit else f'{table["name"]}_pkey'
                if cname not in table['dropped_constraints']: table['pks'].append((col,)); info['nullable'] = False
            if re.search(r'\bUNIQUE\b', attrs, re.I):
                cname = ident(explicit.group(1)) if explicit else f'{table["name"]}_{col}_key'
                if cname not in table['dropped_constraints']: table['uniques'].append((col,))
            fk = re.search(rf'\bREFERENCES\s+(?:(?:public)\.)?({IDENT})(?:\s*\(([^)]*)\))?', attrs, re.I)
            if fk:
                cname = ident(explicit.group(1)) if explicit else f'{table["name"]}_{col}_fkey'
                if cname not in table['dropped_constraints']:
                    targets = tuple(columns_list(fk.group(2))) if fk.group(2) else ()
                    table['fks'].append(((col,), ident(fk.group(1)), targets, f'inline:{col}'))
        for con in table['constraints'].values(): parse_constraint_semantics(table, con)
    text = render(tables)
    validate_inventory(tables, text)
    DocSkillProject.open(BASE_DIR).write_markdown('appendices/b-anexo.md', text)
    print(f'{len(files)} migraciones leídas; {len(tables)} tablas reconstruidas; {OUTPUT_PATH}')
    return tables

if __name__ == '__main__': build_anexo_b()
