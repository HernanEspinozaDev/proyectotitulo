#!/usr/bin/env python3
"""BPMN de lectura vertical: una fuente geométrica produce SVG, PNG y BPMN DI.

Proceso ilustrativo no ejecutable. Cada figura cabe a 5,7 pulgadas en una página
vertical; texto de 22 px equivale a 9 puntos al tamaño de inserción.
"""
from pathlib import Path
import json
import math
import textwrap
import xml.etree.ElementTree as ET
from html import escape
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / 'assets/figuras'
SOURCES = ASSETS / 'fuentes'
WIDTH, HEIGHT, SCALE = 1000, 1260, 2
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
B = 'http://www.omg.org/spec/BPMN/20100524/MODEL'
D = 'http://www.omg.org/spec/BPMN/20100524/DI'
DC = 'http://www.omg.org/spec/DD/20100524/DC'
DI = 'http://www.omg.org/spec/DD/20100524/DI'
for prefix, uri in [('bpmn', B), ('bpmndi', D), ('dc', DC), ('di', DI)]:
    ET.register_namespace(prefix, uri)


class Figure:
    def __init__(self, stem, title):
        self.stem, self.title = stem, title
        self.nodes, self.flows = {}, []
        self.im = Image.new('RGB', (WIDTH*SCALE, HEIGHT*SCALE), 'white')
        self.draw = ImageDraw.Draw(self.im)
        self.svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
                    f'<title>{escape(title)}</title>', '<rect width="100%" height="100%" fill="white"/>']
        self.rect((25, 24, 975, 1238), fill='#FFFFFF', stroke='#334155', radius=0)
        self.rect((25, 24, 975, 77), fill='#EEF2F6', stroke='#334155', radius=0)
        self.text((500, 50), title, size=25, bold=True, width=920)

    def rect(self, box, fill='white', stroke='#334155', radius=9, weight=2):
        x1,y1,x2,y2 = box
        self.draw.rounded_rectangle(tuple(v*SCALE for v in box), radius=radius*SCALE,
                                    fill=fill, outline=stroke, width=weight*SCALE)
        self.svg.append(f'<rect x="{x1}" y="{y1}" width="{x2-x1}" height="{y2-y1}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{weight}"/>')

    def text(self, center, value, size=22, bold=False, width=360):
        face = ImageFont.truetype(BOLD if bold else FONT, size*SCALE)
        lines = []
        for para in value.split('\n'):
            line = ''
            for word in para.split():
                candidate = f'{line} {word}'.strip()
                if self.draw.textlength(candidate, font=face) > width*SCALE and line:
                    lines.append(line); line = word
                else: line = candidate
            lines.append(line)
        step = size*1.22
        x, y = center
        for idx, line in enumerate(lines):
            yy = y + (idx-(len(lines)-1)/2)*step
            self.draw.text((x*SCALE, yy*SCALE), line, font=face, fill='#172033', anchor='mm')
            self.svg.append(f'<text x="{x}" y="{yy}" text-anchor="middle" dominant-baseline="central" font-family="DejaVu Sans" font-size="{size}" font-weight="{"bold" if bold else "normal"}" fill="#172033">{escape(line)}</text>')
        return len(lines)*step

    def node(self, key, kind, y, label='', x=600, width=420):
        if kind in ('startEvent', 'endEvent'):
            radius=18
            self.draw.ellipse(((x-radius)*SCALE,(y-radius)*SCALE,(x+radius)*SCALE,(y+radius)*SCALE), fill='white', outline='#334155', width=(4 if kind=='endEvent' else 2)*SCALE)
            self.svg.append(f'<circle cx="{x}" cy="{y}" r="18" fill="white" stroke="#334155" stroke-width="{4 if kind=="endEvent" else 2}"/>')
            bounds=(x-18,y-18,36,36)
            self.text((x+100,y),label or ('Inicio' if kind=='startEvent' else 'Fin'),width=150)
        elif kind=='exclusiveGateway':
            points=[(x,y-26),(x+26,y),(x,y+26),(x-26,y)]
            self.draw.polygon([(a*SCALE,b*SCALE) for a,b in points],fill='#FFF7E5',outline='#334155',width=2*SCALE)
            self.svg.append('<polygon points="'+' '.join(f'{a},{b}' for a,b in points)+'" fill="#FFF7E5" stroke="#334155" stroke-width="2"/>')
            self.text((x,y),'×',size=27,width=45)
            self.text((x+205,y),label,width=285)
            bounds=(x-26,y-26,52,52)
        else:
            h=100 if width<300 else 84 if kind=='subProcess' else 76
            self.rect((x-width/2,y-h/2,x+width/2,y+h/2),fill='#F8FAFC')
            used=self.text((x,y-(10 if kind=='subProcess' else 0)),label,width=width-30)
            if used > h-8-(18 if kind=='subProcess' else 0):
                raise ValueError(f'Texto demasiado alto: {key}: {label}')
            if kind=='subProcess':
                self.rect((x-9,y+h/2-23,x+9,y+h/2-5),radius=0,weight=1)
                self.text((x,y+h/2-14),'+',size=18,width=20)
            bounds=(x-width/2,y-h/2,width,h)
        self.nodes[key]={'kind':kind,'name':label,'bounds':bounds,'center':(x,y)}
        return key

    def edge(self, source, target, label='', points=None):
        a,b=self.nodes[source],self.nodes[target]
        if points is None:
            x,y=a['center']; xx,yy=b['center']
            points=[(x,a['bounds'][1]+a['bounds'][3]),(xx,b['bounds'][1])]
        self.draw.line([(x*SCALE,y*SCALE) for x,y in points],fill='#334155',width=2*SCALE)
        self.svg.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in points)+'" fill="none" stroke="#334155" stroke-width="2"/>')
        x,y=points[-1];px,py=points[-2];angle=math.atan2(y-py,x-px)
        arrow=[(x,y),(x-11*math.cos(angle-.40),y-11*math.sin(angle-.40)),(x-11*math.cos(angle+.40),y-11*math.sin(angle+.40))]
        self.draw.polygon([(a*SCALE,b*SCALE) for a,b in arrow],fill='#334155')
        self.svg.append('<polygon points="'+' '.join(f'{a},{b}' for a,b in arrow)+'" fill="#334155"/>')
        if label:
            if len(points)>2 or points[0][1]==points[1][1]: pos=((points[0][0]+points[1][0])/2,points[0][1]-20)
            else: pos=(points[0][0]+35,(points[0][1]+points[-1][1])/2)
            self.text(pos,label,size=21,width=100)
        self.flows.append({'source':source,'target':target,'name':label,'points':points,'label_center':pos if label else None})

    def branch(self, gate, task, end, label, text):
        y=self.nodes[gate]['center'][1]
        self.node(task,'task',y,text,x=190,width=260)
        self.node(end,'endEvent',y+110,'Fin',x=190)
        self.edge(gate,task,label,[(574,y),(320,y)])
        self.edge(task,end)

    def save(self):
        self.svg.append('</svg>')
        (SOURCES/(self.stem+'.svg')).write_text('\n'.join(self.svg),encoding='utf-8')
        self.im.save(ASSETS/(self.stem+'.png'),dpi=(300,300))
        (SOURCES/(self.stem+'.layout.json')).write_text(json.dumps({'title':self.title,'nodes':self.nodes,'flows':self.flows},ensure_ascii=False,indent=2)+'\n')
        definitions=ET.Element(f'{{{B}}}definitions',id=self.stem,targetNamespace='https://espacigo.local/documentacion/es2')
        process=ET.SubElement(definitions,f'{{{B}}}process',id='Process_1',name=self.title,isExecutable='false')
        for key,node in self.nodes.items():
            el=ET.SubElement(process,f'{{{B}}}{node["kind"]}',id=key,name=node['name'])
            for idx,flow in enumerate(self.flows):
                if flow['target']==key: ET.SubElement(el,f'{{{B}}}incoming').text=f'Flow_{idx}'
                if flow['source']==key: ET.SubElement(el,f'{{{B}}}outgoing').text=f'Flow_{idx}'
        for idx,flow in enumerate(self.flows):
            ET.SubElement(process,f'{{{B}}}sequenceFlow',id=f'Flow_{idx}',sourceRef=flow['source'],targetRef=flow['target'],name=flow['name'])
        collab=ET.SubElement(definitions,f'{{{B}}}collaboration',id='Collaboration_1')
        ET.SubElement(collab,f'{{{B}}}participant',id='Participant_1',name='espaciGo',processRef='Process_1')
        diagram=ET.SubElement(definitions,f'{{{D}}}BPMNDiagram',id='Diagram_1')
        plane=ET.SubElement(diagram,f'{{{D}}}BPMNPlane',id='Plane_1',bpmnElement='Collaboration_1')
        pool=ET.SubElement(plane,f'{{{D}}}BPMNShape',id='Shape_Participant',bpmnElement='Participant_1',isHorizontal='true')
        ET.SubElement(pool,f'{{{DC}}}Bounds',x='25',y='24',width='950',height='1214')
        for key,node in self.nodes.items():
            shape=ET.SubElement(plane,f'{{{D}}}BPMNShape',id='Shape_'+key,bpmnElement=key)
            if node['kind']=='subProcess':shape.set('isExpanded','false')
            x,y,w,h=node['bounds'];ET.SubElement(shape,f'{{{DC}}}Bounds',x=str(x),y=str(y),width=str(w),height=str(h))
            if node['kind'] in ['exclusiveGateway','startEvent','endEvent']:
                x,y=node['center']; lab=ET.SubElement(shape,f'{{{D}}}BPMNLabel')
                ET.SubElement(lab,f'{{{DC}}}Bounds',x=str(x+62 if node['kind']=='exclusiveGateway' else x+30),y=str(y-40 if node['kind']=='exclusiveGateway' else y-16),width='285' if node['kind']=='exclusiveGateway' else '150',height='80' if node['kind']=='exclusiveGateway' else '32')
        for idx,flow in enumerate(self.flows):
            edge=ET.SubElement(plane,f'{{{D}}}BPMNEdge',id=f'Edge_{idx}',bpmnElement=f'Flow_{idx}')
            for x,y in flow['points']:ET.SubElement(edge,f'{{{DI}}}waypoint',x=str(x),y=str(y))
            if flow['label_center']:
                x,y=flow['label_center']; lab=ET.SubElement(edge,f'{{{D}}}BPMNLabel')
                ET.SubElement(lab,f'{{{DC}}}Bounds',x=str(x-30),y=str(y-15),width='60',height='30')
        ET.indent(definitions)
        ET.ElementTree(definitions).write(SOURCES/(self.stem+'.bpmn'),encoding='utf-8',xml_declaration=True)


def reservation():
    f=Figure('fig01_bpmn_reserva_escrow_operacion','Reserva y operación de arriendo · espaciGo')
    specs=[('inicio','startEvent',120,'Inicio'),('cotizacion','task',195,'Recibir solicitud y\nvalidar cotización'),('disponible','exclusiveGateway',275,'¿Intervalo\ndisponible?'),('reserva','task',365,'Crear reserva y\nretener intervalo'),('pago','subProcess',475,'Gestionar pago y\nvencimiento de retención'),('pagada','exclusiveGateway',585,'¿Pago confirmado\ndentro del plazo?'),('host','task',680,'Recibir decisión\ndel anfitrión'),('aceptada','exclusiveGateway',775,'¿Solicitud\naprobada?'),('contrato','subProcess',870,'Formalizar contrato\ny firmas de las partes'),('operacion','subProcess',975,'Registrar check-in,\ncheck-out y recepción'),('liquidacion','subProcess',1080,'Resolver liquidación\no disputa, según evidencia'),('fin','endEvent',1195,'Fin')]
    for spec in specs:f.node(*spec)
    ids=[s[0] for s in specs]
    for a,b in zip(ids,ids[1:]):f.edge(a,b,'Sí' if a in ['disponible','pagada','aceptada'] else '')
    f.branch('disponible','conflicto','fin_conflicto','No','Notificar conflicto\nde disponibilidad')
    f.branch('pagada','vencimiento','fin_vencida','No','Vencer solicitud y\nliberar intervalo')
    f.branch('aceptada','devolucion','fin_rechazada','No','Liberar intervalo y\ngestionar devolución')
    f.save()


def publication():
    f=Figure('fig02_bpmn_publicacion_kyc_moderacion','Publicación y verificación · espaciGo')
    specs=[('inicio','startEvent',120,'Inicio'),('solicitud','task',200,'Recibir ficha del espacio\ny antecedentes'),('borrador','task',310,'Validar datos y\ncrear borrador'),('medios','subProcess',420,'Procesar fotografías\ny variantes de medios'),('verificacion','subProcess',530,'Revisar antecedentes\nde identidad KYC/KYB'),('identidad','exclusiveGateway',640,'¿Verificación\naprobada?'),('moderacion','task',750,'Evaluar requisitos de\npublicación y moderación'),('aprobacion','exclusiveGateway',855,'¿Publicación\nautorizada?'),('publicar','task',965,'Publicar espacio y\nactualizar catálogo'),('fin','endEvent',1100,'Fin')]
    for spec in specs:f.node(*spec)
    ids=[s[0] for s in specs]
    for a,b in zip(ids,ids[1:]):f.edge(a,b,'Sí' if a in ['identidad','aprobacion'] else '')
    f.branch('identidad','observacion_kyc','fin_kyc','No','Comunicar\nobservaciones KYC/KYB')
    f.branch('aprobacion','observacion_espacio','fin_espacio','No','Comunicar ajustes\ny conservar borrador')
    f.save()


def privacy():
    f=Figure('fig03_bpmn_supresion_datos_ley21719','Solicitud de supresión de datos · espaciGo')
    specs=[('inicio','startEvent',120,'Inicio'),('registro','task',200,'Registrar solicitud\ndel titular'),('identidad','subProcess',310,'Verificar identidad\ny alcance de la solicitud'),('procedente','exclusiveGateway',420,'¿Solicitud\nprocedente?'),('retencion','task',530,'Evaluar obligaciones y\nretención aplicable'),('impedimentos','exclusiveGateway',640,'¿Hay impedimentos\npara la supresión?'),('anonimizar','subProcess',750,'Revocar sesiones y\ndesidentificar datos'),('archivos','subProcess',860,'Purgar archivos y\nevidencias procedentes'),('replay','task',970,'Registrar ejecución\ny replay de bajas'),('respuesta','task',1080,'Notificar resultado\nal titular'),('fin','endEvent',1195,'Fin')]
    for spec in specs:f.node(*spec)
    ids=[s[0] for s in specs]
    for a,b in zip(ids,ids[1:]):f.edge(a,b,('Sí' if a=='procedente' else 'No' if a=='impedimentos' else ''))
    f.branch('procedente','subsanacion','fin_subsanar','No','Comunicar requisitos\nde subsanación')
    f.branch('impedimentos','limitacion','fin_limitado','Sí','Comunicar decisión\nfundada y su alcance')
    f.save()


if __name__=='__main__':
    SOURCES.mkdir(parents=True,exist_ok=True)
    reservation();publication();privacy()
    print('Tres BPMN verticales generados: SVG, PNG, geometría y modelo BPMN 2.0 no ejecutable.')
