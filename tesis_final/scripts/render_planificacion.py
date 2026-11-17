"""Figuras reproducibles de planificación desde el registro maestro y su cálculo."""
from pathlib import Path
import json
from datetime import datetime, timedelta
import textwrap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from matplotlib.patches import FancyArrowPatch
ROOT=Path(__file__).resolve().parents[2]
M=json.loads((ROOT/'tesis_final/assets/diagramas_src/cronograma_espacigo.json').read_text())
C=json.loads((ROOT/'preparacion_planificacion_pmbok/04_ejecucion/calculo_cronograma.json').read_text())
OUT=ROOT/'tesis_final/assets/figuras'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11.5,'svg.fonttype':'none'})

def save(fig,name):
    for ext in ['png','svg']:fig.savefig(OUT/(name+'.'+ext),dpi=230,bbox_inches='tight',facecolor='white')
    svg=OUT/(name+'.svg')
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines())+'\n')
    plt.close(fig)

def dt(s):return datetime.fromisoformat(s[:10])

def gantt(rows,name,summary=False):
    fig,ax=plt.subplots(figsize=(8,max(5,len(rows)*.34+1.5)))
    start=dt('2026-08-01');finish=dt('2027-01-05')
    for i,r in enumerate(rows):
        a=dt(r['inicio']);b=dt(r['fin']); critical=r.get('holgura_red_nivelada')==0
        color={'base':'#35729a','defensa':'#6b559a','transicion':'#62844c','comercial':'#62844c'}[r['etapa']]
        if r.get('tipo')=='hito':ax.plot(a,i,marker='D',color='#333333',markersize=6)
        else:ax.barh(i,max(1,(b-a).days+1),left=dates.date2num(a),height=.62,color=color,edgecolor='#222222',linewidth=.6,hatch='///' if critical else '')
    ax.set_yticks(range(len(rows)),[r['id']+'  '+textwrap.shorten(r['nombre'],width=35,placeholder='…') for r in rows]);ax.invert_yaxis()
    ax.set_xlim(start,finish);ax.xaxis.set_major_locator(dates.MonthLocator());ax.xaxis.set_major_formatter(dates.DateFormatter('%m/%Y'))
    ax.xaxis.set_minor_locator(dates.WeekdayLocator(byweekday=dates.MO));ax.grid(axis='x',which='major',alpha=.5);ax.grid(axis='x',which='minor',alpha=.15)
    for k,label in [('ENT','01 dic'),('DEF','09 dic'),('COM','01 ene')]:
        x=dt(M['hitos_fijos'][k]);ax.axvline(x,ls=':',lw=.8,c='#444444');ax.text(x,-.8,label,rotation=90,fontsize=8,va='bottom',ha='center')
    ax.spines[['top','right']].set_visible(False)
    fig.text(.02,.01,'Referencia 16-11-2026 · barras: programación · trama: holgura cero (cierre académico)\nAzul: desarrollo; violeta: defensa; verde: transición/comercial. Sin avance real inferido.',fontsize=9)
    fig.tight_layout(rect=[0,.08,1,.97]);save(fig,name)

# Resumen por entregables; las barras resumen no acumulan ni duplican esfuerzo.
groups=['Gestión y alcance','Análisis y diseño','Identidad y acceso','Catálogo y búsqueda','Contratación y cobros','Documentos y operación','Administración y auditoría','AWS y aceptación','Informe y evaluación']
print(sorted(set(r['grupo'] for r in C['actividades'])))
summary=[]
for group in groups:
    rr=[r for r in C['actividades'] if r['grupo']==group and r['etapa']=='base' and r['tipo']!='hito']
    if not rr:continue
    summary.append({'id':str(len(summary)+1),'nombre':group,'inicio':min(r['inicio'] for r in rr),'fin':max(r['fin'] for r in rr),'etapa':'base','holgura_red_nivelada':None})
for stage,label in [('defensa','Preparación de defensa'),('transicion','Transición preoperativa')]:
    rr=[r for r in C['actividades'] if r['etapa']==stage and r['tipo']!='hito']
    summary.append({'id':str(len(summary)+1),'nombre':label,'inicio':min(r['inicio'] for r in rr),'fin':max(r['fin'] for r in rr),'etapa':stage,'holgura_red_nivelada':None})
for key in ['ENT','DEF','COM']:summary.append(next(r for r in C['actividades'] if r['id']==key))
gantt(summary,'gantt_maestro',True)
for i in range(3):gantt(C['actividades'][i*21:(i+1)*21],f'gantt_detalle_{i+1}')
# Red del tramo crítico, con bifurcación real Q08->Q09/R03->R04.
fig,ax=plt.subplots(figsize=(8,8.8));ax.set_xlim(0,10);ax.set_ylim(-.5,10.2);ax.axis('off')
positions={'W01':(5,9),'W02':(5,7.4),'Q08':(5,5.8),'Q09':(2.5,4),'R03':(7.5,4),'R04':(5,2),'C0':(5,.4)}
by={r['id']:r for r in C['actividades']};boxes={}
for k,(x,y) in positions.items():
    r=by[k];label=k+'\n'+textwrap.fill(r['nombre'],27)+'\n'+(r['inicio'][8:10]+' nov' if r['inicio'][:10]==r['fin'][:10] else r['inicio'][8:10]+'–'+r['fin'][8:10]+' nov')
    boxes[k]=ax.text(x,y,label,ha='center',va='center',fontsize=11,bbox=dict(boxstyle='round,pad=.4',fc='#eef2f5',ec='#222222')).get_bbox_patch()
for k in positions:
    for p in by[k]['predecesoras']+by[k]['predecesoras_recursos']:
        if p in positions:
            x,y=positions[p];u,v=positions[k];ax.annotate('',xy=(u,v),xytext=(x,y),arrowprops=dict(arrowstyle='->',patchA=boxes[p],patchB=boxes[k],shrinkA=3,shrinkB=3,lw=1))
fig.text(.03,.01,'Dos ramas críticas convergen en R04. El cuadro G.5 contiene toda la red y sus holguras.\nLiberación AWS: 16-11-2026. La disponibilidad de personas se incluye en el cálculo.',fontsize=9);save(fig,'red_critica_planificacion')
# EDT actualizada, con la misma estructura 6 ramas / 28 paquetes.
fig,axes=plt.subplots(3,2,figsize=(8,9.2));titles=['Gobierno','Análisis','Arquitectura y datos','Construcción incremental','Calidad','Transición y cierre']
for n,ax in enumerate(axes.flat,1):
    ax.axis('off');ax.text(0,1,f'1.{n} · {titles[n-1]}',fontsize=13,weight='bold',va='top')
    packs=[p for p in M['paquetes'] if p['id'].startswith(f'1.{n}.')]
    for i,p in enumerate(packs):ax.text(.02,.84-i*.16,p['id']+' '+textwrap.fill(p['nombre'],28),fontsize=12,va='top')
fig.tight_layout();save(fig,'edt_paquetes')
# Mapa coherente con las ocho fichas de riesgos.
fig,ax=plt.subplots(figsize=(7,5.6));values=[[p*i for i in range(1,6)] for p in range(1,6)]
ax.imshow(values,origin='lower',extent=[.5,5.5,.5,5.5],cmap='YlOrRd',alpha=.65,vmin=1,vmax=25)
for p in range(1,6):
    for i in range(1,6):ax.text(i,p-.20,str(i*p),ha='center',fontsize=10)
for x,y,label in [(5,3,'R01'),(5,2,'R02 / R03'),(4,3,'R04 / R06'),(4,1,'R05'),(4,2,'R07 / R08')]:ax.text(x,y+.15,label,ha='center',weight='bold',fontsize=9)
ax.set_xticks(range(1,6));ax.set_yticks(range(1,6));ax.set_xlabel('Impacto (1 menor – 5 crítico)');ax.set_ylabel('Probabilidad (1 muy baja – 5 muy alta)');save(fig,'mapa_riesgos')
