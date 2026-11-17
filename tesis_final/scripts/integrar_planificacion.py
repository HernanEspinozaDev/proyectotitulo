"""Integra la programación calculada en VI/G y XV; conserva la plantilla institucional."""
from pathlib import Path
from datetime import date
import json,re
ROOT=Path(__file__).resolve().parents[2];T=ROOT/'tesis_final';OUT=ROOT/'preparacion_planificacion_pmbok/04_ejecucion'
M=json.loads((T/'assets/diagramas_src/cronograma_espacigo.json').read_text());C=json.loads((OUT/'calculo_cronograma.json').read_text()); BY={r['id']:r for r in C['actividades']}

def fmt(s):return date.fromisoformat(s[:10]).strftime('%d-%m-%Y')
def clp(n):return 'CLP '+f'{n:,.0f}'.replace(',','.')
def table(label,title,headers,rows,note='Elaboración propia a partir del registro maestro del cronograma, corte 16-11-2026.'):
    return f'**Tabla {label}**\\\n*{title}*\n\n| '+' | '.join(headers)+' |\n| '+' | '.join(['---']*len(headers))+' |\n'+''.join('| '+' | '.join(str(x).replace('|','/') for x in row)+' |\n' for row in rows)+f'\n*Nota.* {note}\n\n'
def figure(label,title,file,width='16cm',note='Elaboración propia a partir del modelo de programación de espaciGo. Las barras representan fechas programadas y no avance real.'):
    return f'**Figura {label}**\\\n*{title}*\n\n![](assets/figuras/{file}.png){{width={width}}}\n\n*Nota.* {note}\n\n'
# La narrativa académica permanece en sus capítulos y no se sobrescribe.
# Se actualizan únicamente fichas y tablas del Anexo G desde el modelo.
p=T/'appendices/g-carta-gantt-detallada.md';g=p.read_text()
start=g.index('**EDT 1.1.1.');end=g.index('La revisión de nombres conserva',start)
fiches=''
for pk in M['paquetes']:
    fiches+=f"**EDT {pk['id']}. {pk['nombre']}**\n\n"
    fiches+=f"Responsable de coordinación: {M['personas'][pk['responsable']]['nombre']}. Entregable: {pk['nombre'].lower()}. Criterio de aceptación: {pk['aceptacion']}\n\n"
    fiches+=f"Actividades: {', '.join(pk['actividades'])}. Esfuerzo: {pk['horas']} h; valorización: {clp(pk['horas']*6500)}, diferenciada del pago. Referencia de producto y evidencia: {pk['referencia']}. Recursos: equipo personal, sistema de control de versiones y entorno del componente. Riesgo principal: {pk['riesgo']}. Límite: {pk['limite']}\n\n"
g=g[:start]+fiches+g[end:]
blocks=''
for n in range(0,len(C['actividades']),12):
    rows=C['actividades'][n:n+12]
    blocks+=table(f'G.3.{n//12+1}','Actividades, entregables y origen: parte '+str(n//12+1),['ID / EDT','Actividad','Responsable / h','MPP'],[(r['id']+' / '+r['edt'],r['nombre'],(r['responsable'] or 'Hito')+' / '+str(r['horas']),', '.join(map(str,r['mpp_ids'])) or '—') for r in rows])
start=g.index('**Tabla G.3.1**');end=g.index('El criterio de aceptación de cada actividad',start)
g=g[:start]+blocks+g[end:]
p.write_text(g)
print('Fichas y actividades actualizadas. La narrativa académica de VI/XV y el resto de G se conserva; revisar fechas y síntesis si cambia el modelo.')
