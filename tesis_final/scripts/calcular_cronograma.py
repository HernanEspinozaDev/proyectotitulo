"""Programa el modelo por calendario y recursos; calcula CPM y exporta Project XML."""
from pathlib import Path
from datetime import date, timedelta
from collections import defaultdict
import csv
import hashlib
import json
import math
import xml.etree.ElementTree as X

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT/'tesis_final/assets/diagramas_src/cronograma_espacigo.json'
OUT = ROOT/'preparacion_planificacion_pmbok/04_ejecucion'


def main():
    m=json.loads(SOURCE.read_text()); rows=m['actividades']; by={r['id']:r for r in rows}
    assert len(by)==len(rows)
    days=[];d=date.fromisoformat(m['inicio'])
    while d<=date(2027,3,31):
        if d.weekday() in m['calendario']['dias_semana'] and d.isoformat() not in m['calendario']['excepciones']:days.append(d)
        d+=timedelta(days=1)
    def index(s):
        value=date.fromisoformat(s)
        return next(i for i,d in enumerate(days) if d>=value)
    def stamp(n,finish=False):
        return days[max(0,n-1) if finish and n else n].isoformat()+('T13:00:00' if finish else 'T09:00:00')
    pending=list(by);order=[]
    while pending:
        ready=next((k for k in pending if all(p in order for p in by[k]['predecesoras'])),None)
        if ready is None:raise ValueError('Ciclo o vínculo inexistente')
        order.append(ready);pending.remove(ready)
    load={p:defaultdict(float) for p in m['personas']};scheduled={}
    for k in order:
        r=by[k];duration=math.ceil(r['horas']/4);release=index(r['liberacion']) if r.get('liberacion') else 0
        start=max([release]+[scheduled[p]['ef'] for p in r['predecesoras']])
        owner=r['responsable']
        while duration and any(load[owner][n]+4>4 for n in range(start,start+duration)):start+=1
        finish=start+duration
        for n in range(start,finish):load[owner][n]+=4
        if duration:
            begin, end=stamp(start),stamp(finish,True)
        else:
            begin=end=max(r.get('fecha_compromiso')+'T09:00:00' if r.get('fecha_compromiso') else '0000',stamp(start,True))
        scheduled[k]={**r,'duracion_dias':duration,'es':start,'ef':finish,'inicio':begin,'fin':end,'liberacion_indice':release}
    # Reproducir en el intercambio la secuencia de uso de cada persona.
    resource_edges=[]
    for p in m['personas']:
        owned=sorted([r for r in scheduled.values() if r['responsable']==p],key=lambda r:(r['es'],r['id']))
        for a,b in zip(owned,owned[1:]):
            assert a['ef']<=b['es']
            if a['id'] not in b['predecesoras']:resource_edges.append((a['id'],b['id']))
    augmented={k:list(by[k]['predecesoras']) for k in by}
    for a,b in resource_edges:augmented[b].append(a)
    def cpm(preds,terminal):
        ancestors=set()
        def visit(k):
            if k in ancestors:return
            ancestors.add(k)
            for p in preds[k]:visit(p)
        visit(terminal)
        ordered=[];wait=list(ancestors)
        while wait:
            k=next((k for k in order if k in wait and all(p in ordered for p in preds[k])),None)
            if k is None:raise ValueError('Ciclo en red ampliada')
            ordered.append(k);wait.remove(k)
        es={};ef={};succ=defaultdict(list)
        for k in ordered:
            es[k]=max([scheduled[k]['liberacion_indice']]+[ef[p] for p in preds[k]])
            ef[k]=es[k]+scheduled[k]['duracion_dias']
            for p in preds[k]:succ[p].append(k)
        lf={};ls={}
        for k in reversed(ordered):
            lf[k]=min([ls[s] for s in succ[k]]) if succ[k] else ef[terminal]
            ls[k]=lf[k]-scheduled[k]['duracion_dias']
        return {'fin_indice':ef[terminal],'fin':stamp(ef[terminal],True),'ids_criticos':[k for k in ordered if ls[k]==es[k]],
                'filas':{k:{'es':es[k],'ef':ef[k],'ls':ls[k],'lf':lf[k],'holgura':ls[k]-es[k]} for k in ordered}}
    logical=cpm({k:by[k]['predecesoras'] for k in by},'C0');leveled=cpm(augmented,'C0')
    assert leveled['fin_indice']==scheduled['C0']['ef']
    for k,r in scheduled.items():
        r['predecesoras_recursos']=[a for a,b in resource_edges if b==k]
        r['holgura_red_nivelada']=leveled['filas'].get(k,{}).get('holgura')
        assert all(scheduled[p]['ef']<=r['es'] for p in r['predecesoras'])
    academic=[r for r in scheduled.values() if r['etapa']=='base']
    base_hours={p:sum(r['horas'] for r in academic if r['responsable']==p) for p in m['personas']}
    total_hours={p:sum(r['horas'] for r in scheduled.values() if r['responsable']==p) for p in m['personas']}
    stage_hours={s:sum(r['horas'] for r in scheduled.values() if r['etapa']==s) for s in ['base','defensa','transicion','comercial']}
    capacity=sum(d<=date.fromisoformat(m['fin_base']) for d in days)*4
    assert capacity==320
    assert all(v<=320 for v in base_hours.values())
    overload=[]
    for p,entries in load.items():
        iso=defaultdict(float)
        for n,h in entries.items():
            iso[days[n].isocalendar()[:2]]+=h
            if h>4:overload.append([p,days[n].isoformat(),h])
        assert all(h<=20 for h in iso.values())
    assert not overload
    for k,target in m['hitos_fijos'].items():assert scheduled[k]['es']<=index(target),(k,'plazo incumplido')
    total=sum(stage_hours.values());budget=m['presupuesto_valorizado_horas'];assert total<=budget
    result={'modelo_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'actividades':[scheduled[k] for k in order],
            'calendario_dias':[d.isoformat() for d in days],'horas_por_etapa':stage_hours,
            'horas_base_por_persona':base_hours,'horas_totales_por_persona':total_hours,
            'capacidad_base_por_persona':capacity,'capacidad_base_equipo':capacity*3,
            'capacidad_no_asignada_base':capacity*3-stage_hours['base'],
            'presupuesto_valorizado_horas':budget,'esfuerzo_asignado_total':total,'saldo_presupuesto_horas':budget-total,
            'valoracion_actividades_clp':total*m['tarifa_valoracion_clp'],
            'reserva_presupuestaria_valorizada_clp':(budget-total)*m['tarifa_valoracion_clp'],
            'cpm_logico':logical,'cpm_nivelado':leveled,'vinculos_recursos':resource_edges,
            'margen_entrega_jornadas':index(m['hitos_fijos']['ENT'])-scheduled['C0']['ef'],
            'sobrecargas':overload,'avance_real':'no inferido; campos reales se mantienen sin atribuir ejecución',
            'naturaleza':'Estimación de esfuerzo por juicio técnico adaptado al corte académico, no reconstrucción de horas reales.'}
    result['conciliacion_economica'] = {
        'capacidad_base_horas': capacity*3, 'horas_base_asignadas': stage_hours['base'],
        'horas_defensa': stage_hours['defensa'], 'horas_transicion': stage_hours['transicion'],
        'horas_asignadas_total': total, 'presupuesto_valorizado_horas': budget,
        'tarifa_clp_hora': m['tarifa_valoracion_clp'], 'presupuesto_valorizado_clp': budget*m['tarifa_valoracion_clp'],
        'valor_asignaciones_clp': total*m['tarifa_valoracion_clp'],
        'reserva_presupuestaria_horas': budget-total, 'reserva_presupuestaria_clp': (budget-total)*m['tarifa_valoracion_clp'],
        'capacidad_base_libre_horas': capacity*3-stage_hours['base'],
        'inicio_operacion': m['hitos_fijos']['COM'], 'horas_reales_acreditadas': None,
        'nota': 'Estimación de planificación; la valoración no acredita trabajo real, remuneración ni egreso de caja.'}
    OUT.mkdir(exist_ok=True,parents=True)
    (OUT/'calculo_cronograma.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    with (OUT/'actividades_cronograma.csv').open('w',newline='') as f:
        writer=csv.writer(f,lineterminator="\n");writer.writerow(['ID','EDT','Actividad','Responsable','Inicio programado','Fin programado','Días 4h','Horas','Predecesoras lógicas','Predecesoras recurso','Holgura base','Etapa'])
        for r in result['actividades']:
            writer.writerow([r['id'],r['edt'],r['nombre'],m['personas'].get(r['responsable'],{}).get('nombre','Hito'),r['inicio'],r['fin'],r['duracion_dias'],r['horas'],','.join(r['predecesoras']),','.join(r['predecesoras_recursos']),r['holgura_red_nivelada'],r['etapa']])
    export_xml(m,result)
    print(json.dumps({k:result[k] for k in ['horas_por_etapa','horas_base_por_persona','esfuerzo_asignado_total','saldo_presupuesto_horas','margen_entrega_jornadas']},ensure_ascii=False))


def export_xml(model,result):
    ns='http://schemas.microsoft.com/project';X.register_namespace('',ns)
    def el(parent,key,value):node=X.SubElement(parent,'{'+ns+'}'+key);node.text=str(value);return node
    root=X.Element('{'+ns+'}Project')
    for k,v in [('SaveVersion',14),('Name',model['nombre']),('Title',model['nombre']),('ScheduleFromStart',1),('StartDate','2026-08-11T09:00:00'),('FinishDate','2027-01-01T09:00:00'),('CurrencyDigits',0),('CurrencySymbol','CLP'),('CurrencyCode','CLP'),('CalendarUID',1),('DefaultStartTime','09:00:00'),('DefaultFinishTime','13:00:00'),('MinutesPerDay',240),('MinutesPerWeek',1200),('DaysPerMonth',20)]:el(root,k,v)
    calendars=el(root,'Calendars','');cal=el(calendars,'Calendar','');el(cal,'UID',1);el(cal,'Name','Académico nominal 20 h');el(cal,'IsBaseCalendar',1);el(cal,'BaseCalendarUID',-1)
    week=el(cal,'WeekDays','')
    for day in range(1,8):
        wd=el(week,'WeekDay','');el(wd,'DayType',day);el(wd,'DayWorking',int(day not in [1,7]))
        if day not in [1,7]:
            wt=el(el(wd,'WorkingTimes',''),'WorkingTime','');el(wt,'FromTime','09:00:00');el(wt,'ToTime','13:00:00')
    resources=el(root,'Resources','');rids={key:i+1 for i,key in enumerate(model['personas'])}
    for key,person in model['personas'].items():
        res=el(resources,'Resource','')
        for k,v in [('UID',rids[key]),('ID',rids[key]),('Name',person['nombre']),('Type',1),('MaxUnits',1),('CalendarUID',1)]:el(res,k,v)
    rows=result['actividades'];packages=model.get('paquetes',[])
    package_ids={p['id'] for p in packages}
    grouped={p['id']:[] for p in packages};closures=[]
    for r in rows:
        (grouped[r['edt']] if r.get('edt') in package_ids else closures).append(r)

    # UID de resumen estable por EDT; UID de actividades estable por el orden de
    # origen más un prefijo reservado. Los enlaces siempre apuntan a estos UID.
    summary_uids={p['id']:i+1 for i,p in enumerate(packages)}
    closures_uid=len(packages)+1 if closures else None
    activity_uids={r['id']:100+i for i,r in enumerate(rows)}
    uids={**activity_uids,**summary_uids}
    if closures_uid is not None:uids['Cierres']=closures_uid
    ordered=[]
    for p in packages:
        ordered.append(('summary',p,grouped[p['id']]))
        ordered.extend(('activity',r,None) for r in grouped[p['id']])
    if closures:
        ordered.append(('summary',{'id':'Cierres','nombre':'Cierres'},closures))
        ordered.extend(('activity',r,None) for r in closures)

    def span_hours(start,finish):
        first=date.fromisoformat(start[:10]);last=date.fromisoformat(finish[:10])
        return sum(4 for offset in range((last-first).days+1)
                   if (first+timedelta(days=offset)).weekday()<5)

    tasks=el(root,'Tasks','');outline=0;child_counts={};package_outline={p['id']:i+1 for i,p in enumerate(packages)}
    if closures:package_outline['Cierres']=len(packages)+1
    for kind,item,children in ordered:
        outline+=1
        task=el(tasks,'Task','')
        if kind=='summary':
            child_starts=[c['inicio'] for c in children];child_finishes=[c['fin'] for c in children]
            start=min(child_starts) if child_starts else '2026-08-11T09:00:00'
            finish=max(child_finishes) if child_finishes else start
            uid=summary_uids.get(item['id'],closures_uid)
            wbs=item['id'];name=item['nombre'];duration=span_hours(start,finish)
            outline_number=str(package_outline[item['id']])
            notes=f"EDT {item['id']}; tarea resumen sin asignación ni trabajo imputado."
            fields=[('UID',uid),('ID',outline),('Name',name),('WBS',wbs),('OutlineNumber',outline_number),('OutlineLevel',1),('Start',start),('Finish',finish),('Duration',f"PT{duration}H0M0S"),('DurationFormat',7),('Work','PT0H0M0S'),('Milestone',0),('Summary',1),('Notes',notes)]
        else:
            r=item;parent_wbs=r['edt'] if r.get('edt') in package_ids else 'Cierres'
            child_counts[parent_wbs]=child_counts.get(parent_wbs,0)+1
            local_index=child_counts[parent_wbs]
            wbs=f"{parent_wbs}.{local_index}"
            outline_number=f"{package_outline[parent_wbs]}.{local_index}"
            uid=activity_uids[r['id']];duration=r['horas']
            notes=f"ID estable: {r['id']}; EDT: {r.get('edt','')}; {r['estado']} Las horas son estimadas y no acreditan trabajo real ni remuneración."
            fields=[('UID',uid),('ID',outline),('Name',r['id']+' — '+r['nombre']),('WBS',wbs),('OutlineNumber',outline_number),('OutlineLevel',2),('Start',r['inicio']),('Finish',r['fin']),('Duration',f"PT{duration}H0M0S"),('DurationFormat',7),('Work',f"PT{r['horas']}H0M0S"),('Milestone',int(r['tipo']=='hito')),('Summary',0),('Notes',notes)]
        for k,v in fields:el(task,k,v)
        if kind=='activity' and r.get('liberacion'):
            el(task,'ConstraintType',4);el(task,'ConstraintDate',r['liberacion']+'T09:00:00')
        if kind=='activity' and r.get('fecha_compromiso'):el(task,'Deadline',r['fecha_compromiso']+'T13:00:00')
        if kind=='activity':
            for pred in r['predecesoras']+r['predecesoras_recursos']:
                link=el(task,'PredecessorLink','');el(link,'PredecessorUID',activity_uids[pred]);el(link,'Type',1);el(link,'CrossProject',0)
    assignments=el(root,'Assignments','')
    for i,r in enumerate(rows):
        if not r['responsable']:continue
        a=el(assignments,'Assignment','')
        for k,v in [('UID',i+1),('TaskUID',activity_uids[r['id']]),('ResourceUID',rids[r['responsable']]),('Units',1),('Start',r['inicio']),('Finish',r['fin']),('Work',f"PT{r['horas']}H0M0S")]:el(a,k,v)
    X.indent(root);X.ElementTree(root).write(OUT/'Cronograma_espaciGo_Project.xml',encoding='utf-8',xml_declaration=True)


if __name__=='__main__':main()
