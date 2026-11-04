import re
from pathlib import Path
from collections import OrderedDict

mig_dir = Path('/home/nandev/Documentos/projects/espaciGo/db/migrations')
sql_files = sorted(list(mig_dir.glob('V*.sql')))

tables = OrderedDict()

def extract_constraint_name(con_str):
    m = re.match(r'^CONSTRAINT\s+([a-zA-Z0-9_]+)', con_str, re.I)
    if m:
        return m.group(1).lower()
    # check if inline PRIMARY KEY
    if con_str.upper().startswith('PRIMARY KEY'):
        return 'pkey'
    return None

for f in sql_files:
    v_num = int(f.name.split('__')[0][1:])
    text = f.read_text(encoding='utf-8')
    text_clean = re.sub(r'--.*?$', '', text, flags=re.MULTILINE)
    
    # CREATE TABLE
    for m in re.finditer(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?(?:public\.)?([a-zA-Z0-9_]+)\s*\((.*?)\);', text_clean, re.DOTALL | re.IGNORECASE):
        tname = m.group(1).lower()
        body = m.group(2).strip()
        
        if tname not in tables:
            tables[tname] = {
                'v_created': v_num,
                'columns': OrderedDict(),
                'constraints': OrderedDict(), # con_name -> con_sql
                'pks': set(),
                'fks': {},
                'uqs': set(),
                'gists': set(),
            }
            
        # split column/constraint definitions
        items = []
        curr = []
        p_depth = 0
        for ch in body:
            if ch == '(': p_depth += 1
            elif ch == ')': p_depth -= 1
            elif ch == ',' and p_depth == 0:
                items.append(''.join(curr).strip())
                curr = []
                continue
            curr.append(ch)
        if curr:
            items.append(''.join(curr).strip())
            
        for item in items:
            item = item.strip()
            if not item: continue
            up = item.upper()
            if up.startswith(('CONSTRAINT', 'PRIMARY KEY', 'FOREIGN KEY', 'CHECK', 'UNIQUE', 'EXCLUDE')):
                cname = extract_constraint_name(item)
                if not cname:
                    cname = f'anon_{len(tables[tname]["constraints"])+1}'
                tables[tname]['constraints'][cname] = item
            else:
                # column definition
                tokens = item.split(None, 2)
                if len(tokens) >= 2:
                    col_name = tokens[0].lower().strip('"')
                    if re.match(r'^[a-zA-Z0-9_]+$', col_name):
                        col_type = tokens[1]
                        col_rest = tokens[2] if len(tokens) > 2 else ''
                        nullable = 'NULL' if 'NOT NULL' not in col_rest.upper() else 'NOT NULL'
                        is_pk = 'PRIMARY KEY' in col_rest.upper()
                        if is_pk:
                            nullable = 'NOT NULL'
                            tables[tname]['pks'].add(col_name)
                        m_ref = re.search(r'REFERENCES\s+(?:public\.)?([a-zA-Z0-9_]+)', col_rest, re.I)
                        if m_ref:
                            tables[tname]['fks'][col_name] = m_ref.group(1).lower()
                        tables[tname]['columns'][col_name] = {
                            'type': col_type,
                            'nullable': nullable,
                            'is_pk': is_pk,
                            'rest': col_rest
                        }
                        
    # ALTER TABLE
    for m in re.finditer(r'ALTER\s+TABLE\s+(?:IF\s+EXISTS\s+)?(?:public\.)?([a-zA-Z0-9_]+)\s+([^;]+);', text_clean, re.DOTALL | re.IGNORECASE):
        tname = m.group(1).lower()
        if tname not in tables:
            continue
        body = m.group(2).strip()
        
        # split actions by comma outside parentheses
        actions = []
        curr = []
        p_depth = 0
        for ch in body:
            if ch == '(': p_depth += 1
            elif ch == ')': p_depth -= 1
            elif ch == ',' and p_depth == 0:
                actions.append(''.join(curr).strip())
                curr = []
                continue
            curr.append(ch)
        if curr:
            actions.append(''.join(curr).strip())
            
        for act in actions:
            act = act.strip()
            act_up = act.upper()
            if act_up.startswith('ADD COLUMN'):
                col_def = act[10:].strip()
                if col_def.upper().startswith('IF NOT EXISTS'):
                    col_def = col_def[13:].strip()
                tokens = col_def.split(None, 2)
                if len(tokens) >= 2:
                    cname = tokens[0].lower().strip('"')
                    if re.match(r'^[a-zA-Z0-9_]+$', cname):
                        ctype = tokens[1]
                        rest = tokens[2] if len(tokens) > 2 else ''
                        nullable = 'NULL' if 'NOT NULL' not in rest.upper() else 'NOT NULL'
                        is_pk = 'PRIMARY KEY' in rest.upper()
                        if is_pk:
                            nullable = 'NOT NULL'
                            tables[tname]['pks'].add(cname)
                        m_ref = re.search(r'REFERENCES\s+(?:public\.)?([a-zA-Z0-9_]+)', rest, re.I)
                        if m_ref:
                            tables[tname]['fks'][cname] = m_ref.group(1).lower()
                        tables[tname]['columns'][cname] = {
                            'type': ctype,
                            'nullable': nullable,
                            'is_pk': is_pk,
                            'rest': rest
                        }
            elif act_up.startswith('DROP COLUMN'):
                col_def = act[11:].strip()
                if col_def.upper().startswith('IF EXISTS'):
                    col_def = col_def[9:].strip()
                cname = col_def.split()[0].lower().strip('"')
                if cname in tables[tname]['columns']:
                    del tables[tname]['columns'][cname]
            elif act_up.startswith('ALTER COLUMN'):
                rest_cmd = act[12:].strip()
                parts = rest_cmd.split(None, 1)
                if len(parts) >= 2:
                    cname = parts[0].lower().strip('"')
                    op = parts[1].strip()
                    op_up = op.upper()
                    if cname in tables[tname]['columns']:
                        if 'DROP NOT NULL' in op_up:
                            tables[tname]['columns'][cname]['nullable'] = 'NULL'
                        elif 'SET NOT NULL' in op_up:
                            tables[tname]['columns'][cname]['nullable'] = 'NOT NULL'
                        elif op_up.startswith('TYPE ') or op_up.startswith('SET DATA TYPE '):
                            new_type = op.split()[-1]
                            tables[tname]['columns'][cname]['type'] = new_type
            elif act_up.startswith('DROP CONSTRAINT'):
                con_def = act[15:].strip()
                if con_def.upper().startswith('IF EXISTS'):
                    con_def = con_def[9:].strip()
                con_name = con_def.split()[0].lower().strip('"')
                if con_name in tables[tname]['constraints']:
                    del tables[tname]['constraints'][con_name]
            elif act_up.startswith('ADD CONSTRAINT') or act_up.startswith('ADD PRIMARY KEY') or act_up.startswith('ADD FOREIGN KEY') or act_up.startswith('ADD UNIQUE'):
                clean_act = re.sub(r'^ADD\s+', '', act, flags=re.I).strip()
                cname = extract_constraint_name(clean_act)
                if not cname:
                    cname = f'anon_{len(tables[tname]["constraints"])+1}'
                tables[tname]['constraints'][cname] = clean_act

print(f'Total tables extracted: {len(tables)}')
# Check V000042 specifically:
bloq_col = tables['bloqueo_cuenta_administrativo_local']['columns']['bloqueada_por']
print('bloqueada_por nullable:', bloq_col['nullable'])
hist_col = tables['bloqueo_cuenta_historial_local']['columns']['actor_id']
print('actor_id nullable:', hist_col['nullable'])

# Check verificacion constraints
verif_cons = tables['verificacion']['constraints']
print('verificacion constraints count:', len(verif_cons))
for cname, csql in verif_cons.items():
    if 'estado_ck' in cname:
        print(cname, '->', repr(csql))
