"""Extrae en lectura los datos del MPP y conserva evidencia de su integridad.

Entorno aislado: Python con mpxj==16.10.0, JPype1==1.7.1 y Java disponible.
No recalcula el cronograma ni escribe sobre el archivo recibido.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.metadata
import json

import jpype
import mpxj

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=Path)
    args = parser.parse_args()
    source = args.source.resolve(strict=True)
    output = ROOT/'01_extraccion'
    output.mkdir(exist_ok=True, parents=True)
    before = hashlib.sha256(source.read_bytes()).hexdigest()
    jpype.startJVM('--enable-native-access=ALL-UNNAMED')
    from org.mpxj.reader import UniversalProjectReader
    from org.mpxj.json import JsonWriter
    project = UniversalProjectReader().read(str(source))
    JsonWriter().write(project, str(output/'proyecto_mpxj.json'))

    def value(obj, method):
        result = getattr(obj, method)()
        if result is None:
            return None
        if isinstance(result, bool):
            return result
        return str(result)

    tasks = []
    successors = {}
    for task in project.getTasks():
        predecessors = []
        for relation in task.getPredecessors():
            previous = relation.getPredecessorTask()
            predecessors.append({'id': int(previous.getID()), 'tipo': str(relation.getType()), 'desfase': str(relation.getLag())})
            successors.setdefault(int(previous.getID()), []).append(int(task.getID()))
        tasks.append({
            'id': int(task.getID()), 'uid': int(task.getUniqueID()), 'nombre': str(task.getName()),
            'wbs': value(task, 'getWBS'), 'padre_id': None if task.getParentTask() is None else int(task.getParentTask().getID()),
            'resumen': bool(task.getSummary()), 'hito': bool(task.getMilestone()),
            'inicio': value(task, 'getStart'), 'fin': value(task, 'getFinish'),
            'duracion': value(task, 'getDuration'), 'critica': bool(task.getCritical()),
            'holgura': value(task, 'getTotalSlack'), 'porcentaje_completo': value(task, 'getPercentageComplete'),
            'trabajo_tarea': value(task, 'getWork'), 'inicio_real': value(task, 'getActualStart'),
            'fin_real': value(task, 'getActualFinish'), 'inicio_linea_base': value(task, 'getBaselineStart'),
            'fin_linea_base': value(task, 'getBaselineFinish'), 'modo': value(task, 'getTaskMode'),
            'restriccion': value(task, 'getConstraintType'), 'fecha_restriccion': value(task, 'getConstraintDate'),
            'fecha_limite': value(task, 'getDeadline'), 'predecesoras': predecessors,
        })
    for task in tasks:
        task['sucesoras'] = successors.get(task['id'], [])
    assignments = []
    for a in project.getResourceAssignments():
        resource = a.getResource()
        assignments.append({'tarea_id': int(a.getTask().getID()),
                            'recurso_uid': None if resource is None else int(resource.getUniqueID()),
                            'recurso_nombre': None if resource is None else value(resource, 'getName'),
                            'unidades': value(a, 'getUnits'), 'trabajo': value(a, 'getWork'),
                            'inicio': value(a, 'getStart'), 'fin': value(a, 'getFinish')})
    properties = project.getProjectProperties()
    record = {'archivo': str(source), 'sha256': before,
              'lector': 'MPXJ '+importlib.metadata.version('mpxj'),
              'propiedades': {m.removeprefix('get'): value(properties, m) for m in ['getProjectTitle', 'getStartDate', 'getFinishDate', 'getStatusDate', 'getMinutesPerDay', 'getMinutesPerWeek', 'getDaysPerMonth', 'getCurrencySymbol']},
              'tareas': tasks, 'asignaciones': assignments,
              'recursos': [{'uid': int(r.getUniqueID()), 'nombre': value(r, 'getName'), 'capacidad': value(r, 'getMaxUnits')} for r in project.getResources()]}
    assert hashlib.sha256(source.read_bytes()).hexdigest() == before
    record['archivo_original_sin_cambios'] = True
    (output/'extraccion_normalizada.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'tareas': len(tasks), 'asignaciones': len(assignments), 'sha256': before, 'original_sin_cambios': True}, ensure_ascii=False))
    jpype.shutdownJVM()


if __name__ == '__main__':
    main()
