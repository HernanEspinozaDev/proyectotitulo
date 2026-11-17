"""Comprueba la red extraída y prepara un inventario legible sin recalcular el MPP."""
from pathlib import Path
from datetime import datetime
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]


def main():
    data = json.loads((ROOT/'01_extraccion/extraccion_normalizada.json').read_text())
    tasks = data['tareas']
    by_id = {t['id']: t for t in tasks}
    leaf = [t for t in tasks if not t['resumen']]
    work = [t for t in leaf if not t['hito']]
    # Una red sin ciclos puede seguir siendo incompleta respecto del alcance.
    visited, pending = set(), set()
    def visit(t):
        assert t['id'] not in pending, 'Ciclo en dependencias'
        if t['id'] in visited:
            return
        pending.add(t['id'])
        for p in t['predecesoras']:
            assert p['id'] in by_id
            visit(by_id[p['id']])
        pending.remove(t['id'])
        visited.add(t['id'])
    for task in tasks:
        visit(task)
    fs_violations = []
    for task in leaf:
        for rel in task['predecesoras']:
            pred = by_id[rel['id']]
            if rel['tipo'] == 'FS' and datetime.fromisoformat(task['inicio']) < datetime.fromisoformat(pred['fin']):
                fs_violations.append([pred['id'], task['id']])
    assert not fs_violations
    critical = [t for t in leaf if t['critica']]
    hours = sum(float(a['trabajo'].removesuffix('h')) for a in data['asignaciones'])
    results = {
        'archivo_sha256': data['sha256'],
        'tareas_con_resumen_proyecto': len(tasks), 'filas_sin_resumen_proyecto': len(tasks)-1,
        'fases_resumen': sum(t['resumen'] and t['id'] != 0 for t in tasks),
        'actividades_operativas': len(work), 'hitos': sum(t['hito'] for t in leaf),
        'dependencias': sum(len(t['predecesoras']) for t in tasks),
        'red_sin_ciclos': True, 'violaciones_fecha_en_vinculos_fs_existentes': fs_violations,
        'ids_ruta_critica_almacenada': [t['id'] for t in critical],
        'duracion_ruta_critica_almacenada_dias': sum(float(t['duracion'].removesuffix('d')) for t in critical),
        'trabajo_asignaciones_horas': hours,
        'recursos_con_nombre': sum(bool(r['nombre']) for r in data['recursos']),
        'actividades_sin_sucesora_excluido_cierre_documental': [t['id'] for t in work if not t['sucesoras'] and t['id'] != 32],
        'lineas_base_con_fecha_inicio': sum(t['inicio_linea_base'] is not None for t in tasks),
        'tareas_con_inicio_real': sum(t['inicio_real'] is not None for t in tasks),
        'tareas_con_fin_real': sum(t['fin_real'] is not None for t in tasks),
        'porcentajes_registrados': sorted({t['porcentaje_completo'] for t in tasks}),
        'fecha_estado': data['propiedades']['StatusDate'],
        'moneda': data['propiedades']['CurrencySymbol'],
        'alcance': 'Lectura de la planificación almacenada; no certifica avance, esfuerzo real ni un cronograma actualizado.'}
    assert hashlib.sha256(Path(data['archivo']).read_bytes()).hexdigest() == data['sha256']
    (ROOT/'01_extraccion/resultados_auditoria.json').write_text(json.dumps(results, ensure_ascii=False, indent=2)+'\n')
    md = '# Inventario de tareas extraído de espacigo.mpp\n\nLos ID corresponden a las filas de Project. El ID 0 es el resumen del proyecto. No se modifican nombres, fechas ni dependencias.\n\n'
    md += '| ID | EDT/WBS | Tipo | Nombre original | Inicio | Fin | Duración | Predecesoras | Holgura |\n|---|---|---|---|---|---|---|---|---|\n'
    for t in tasks:
        kind = 'Resumen' if t['resumen'] else 'Hito' if t['hito'] else 'Actividad'
        md += '| '+' | '.join([str(t['id']),t['wbs'],kind,t['nombre'].replace('|','/'),t['inicio'].replace('T',' '),t['fin'].replace('T',' '),t['duracion'],', '.join(str(r['id'])+' '+r['tipo'] for r in t['predecesoras']) or '—',t['holgura']])+' |\n'
    (ROOT/'01_extraccion/INVENTARIO_TAREAS.md').write_text(md)
    print(json.dumps(results, ensure_ascii=False))


if __name__ == '__main__':
    main()
