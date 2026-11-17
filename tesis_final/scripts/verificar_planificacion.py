"""Auditoría independiente de integridad de fuente, programación y documento integrado."""
from pathlib import Path
from collections import defaultdict
from datetime import date,timedelta
import hashlib,json,re,subprocess,xml.etree.ElementTree as E,zipfile
ROOT=Path(__file__).resolve().parents[2];T=ROOT/'tesis_final';OUT=ROOT/'preparacion_planificacion_pmbok/04_ejecucion'
M=json.loads((T/'assets/diagramas_src/cronograma_espacigo.json').read_text());C=json.loads((OUT/'calculo_cronograma.json').read_text())
by={r['id']:r for r in C['actividades']};assert len(by)==63
assert hashlib.sha256((T/'assets/diagramas_src/cronograma_espacigo.json').read_bytes()).hexdigest()==C['modelo_sha256']
assert len(M['paquetes'])==28 and sum(p['horas'] for p in M['paquetes'])==708
assert sum(r['horas'] for r in by.values())==708
for p in M['paquetes']:assert sum(by[k]['horas'] for k in p['actividades'])==p['horas']
original=json.loads((ROOT/'revision_gantt_erick/01_extraccion/extraccion_normalizada.json').read_text())
leafids={r['id'] for r in original['tareas'] if not r['resumen']}
accounted={i for r in by.values() for i in r['mpp_ids']} | {int(k) for k in M['origen_mpp']['tratamiento_hitos']}
assert leafids <= accounted
assigned=[k for p in M['paquetes'] for k in p['actividades']];assert len(assigned)==len(set(assigned))==54
load=defaultdict(int);weeks=defaultdict(int)
for r in by.values():
    for key in ['inicio_real','fin_real','avance_real']:assert r[key] is None
    assert all(by[k]['ef']<=r['es'] for k in r['predecesoras']+r['predecesoras_recursos'])
    if not r['horas']:continue
    d=date.fromisoformat(r['inicio'][:10]);end=date.fromisoformat(r['fin'][:10]);days=[]
    while d<=end:
        if d.weekday()<5 and d.isoformat() not in M['calendario']['excepciones']:days.append(d)
        d+=timedelta(days=1)
    assert len(days)*4==r['horas'],r['id']
    for d in days:load[(r['responsable'],d)]+=4;weeks[(r['responsable'],d.isocalendar()[:2])]+=4
assert max(load.values())==4 and max(weeks.values())<=20
for k,target in M['hitos_fijos'].items():assert by[k]['inicio'][:10]==by[k]['fin'][:10]==target
assert by['C0']['fin'][:10]=='2026-11-30'
# Compare XML independently, including assignment work rather than duplicated summary work.
ns={'p':'http://schemas.microsoft.com/project'};xml=E.parse(OUT/'Cronograma_espaciGo_Project.xml').getroot()
assert len(xml.findall('p:Resources/p:Resource',ns))==3
assignments=xml.findall('p:Assignments/p:Assignment',ns);assert len(assignments)==54
assert sum(float(a.find('p:Work',ns).text.split('H')[0][2:]) for a in assignments)==708
leaf=[r for r in xml.findall('p:Tasks/p:Task',ns) if r.find('p:Summary',ns).text=='0'];assert len(leaf)==63
for node in leaf:
    k=node.find('p:Name',ns).text.split(' — ')[0];r=by[k]
    assert node.find('p:Start',ns).text==r['inicio'] and node.find('p:Finish',ns).text==r['fin']
# Comprobar fuente manuscrita completa y remisiones.
manifest=json.loads((T/'document.json').read_text());sources=[T/p for p in manifest['sections']];text='\n'.join(p.read_text() for p in sources)
tables=re.findall(r'\*\*Tabla ([\dA-H.]+)\*\*',text);figs=re.findall(r'\*\*Figura ([\dA-H.]+)\*\*',text)
assert len(tables)==len(set(tables)),[k for k in tables if tables.count(k)>1]
assert len(figs)==len(set(figs))
assert sorted(int(k) for k in tables if k.isdigit())==list(range(1,25))
assert sorted(int(k) for k in figs if k.isdigit())==list(range(1,20))
for kind,known in [('Tabla',set(tables)),('Figura',set(figs))]:
    for match in re.finditer(kind+r' ((?:[A-H]\.)?\d+(?:\.\d+)?)\b',text):assert match[1] in known,(kind,match[1])
for p in sources:
    for match in re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)',p.read_text()):
        assert not match[1],p
        path=T/match[2];assert path.exists() or (p.parent/match[2]).exists(),path
assert '[@pmbok7' not in text and '7ma Edición' not in text
for path in ['sections/06-capitulo-vi.md','sections/15-capitulo-xv.md','appendices/g-carta-gantt-detallada.md']:assert 'RESERVAD' not in (T/path).read_text()
# Las 27 cuadrículas económicas mantienen exactamente sus datos respecto del corte previo.
for rel in ['sections/14-capitulo-xiv.md','appendices/h-evaluacion-economica-detallada.md']:
    previous=subprocess.check_output(['git','show','b252b62:tesis_final/'+rel],cwd=ROOT,text=True)
    grids=lambda s:[line for line in s.splitlines() if line.startswith('|')]
    assert grids(previous)==grids((T/rel).read_text()),rel
# El marco institucional es idéntico al corte autorizado.
for rel in ['document.json','templates/reference-tihi84.docx','templates/style-profile-inacap.json']:
    previous=subprocess.check_output(['git','show','b252b62:tesis_final/'+rel],cwd=ROOT)
    if rel=='document.json':
        before,after=json.loads(previous),json.loads((T/rel).read_text())
        assert after['metadata']['title']=='Diseño de una plataforma web transaccional para la intermediación y gestión del arriendo flexible de espacios en Chile: espaciGo'
        before['metadata']['title']=after['metadata']['title'];assert before==after,rel
    else:
        assert previous==(T/rel).read_bytes(),rel
result={'estado':'verificado','paquetes_edt':28,'actividades':54,'hitos':9,'horas':708,'sobrecargas':0,'horas_reales_inferidas':False,'margen_entrega_jornadas':0,'tablas_financieras_preservadas':27,'tablas_fuente':len(tables),'figuras_fuente':len(figs),'plantilla_institucional':'preservada','xml':'fechas, 63 hojas, 54 asignaciones y 708 horas comprobadas','limitacion':'Calendario nominal de dedicación sin excepciones personales acreditadas; cero margen de entrega; no implica producción habilitada.'}
(OUT/'verificacion_integracion_planificacion.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False))
