"""Fuentes editables del plan académico. Las estimaciones no son horas reales."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT/'tesis_final/assets/diagramas_src/cronograma_espacigo.json'

PACKAGES = [
('1.1.1','Acuerdo de gobierno y equipo','A','Propósito, responsables, restricciones y decisiones identificados.','VI 6.1.6'),
('1.1.2','Enunciado de alcance y EDT','A','28 paquetes identificados y relacionados con los objetivos.','V; VI 6.1.4'),
('1.1.3','Modelo del cronograma','E','Calendarios, dependencias, hitos, holguras y recursos comprobados.','VI 6.2; G'),
('1.1.4','Presupuesto y criterios de adquisición','A','Partidas y servicios diferenciados sin duplicar valor y caja.','XIV; H'),
('1.1.5','Registro de riesgos y cambios','E','Dueño, disparador, respuesta y versión de cada cambio registrados.','VI 6.1.5–6.1.6; G'),
('1.2.1','Diagnóstico y procesos de referencia','A','Problema, segmentos y BPMN vinculados con la solución.','I–II'),
('1.2.2','Especificación funcional','A','236 RQF identificados con alcance verificable y trazabilidad.','III; A'),
('1.2.3','Especificación de calidad','E','43 RNF relacionados con medición, escenario y aceptación.','III; XI; A'),
('1.2.4','Historias y casos de uso','A','35 HU y 52 CU identificados, con escenarios y aceptación.','III; B–C'),
('1.2.5','Matriz de trazabilidad','A','Objetivo, requisito, caso, componente y prueba relacionados.','XI–XII; A–F'),
('1.3.1','Vistas de arquitectura empresarial','H','Procesos, aplicaciones, datos e infraestructura diferenciados.','VIII'),
('1.3.2','Arquitectura de software','H','Dominio y adaptadores identificados en Go y Next.js.','VII; IX–X'),
('1.3.3','Modelo relacional y geoespacial','H','DDL, restricciones e inventario documentados por versión.','X; D'),
('1.3.4','Diseño de seguridad y privacidad','E','Sesiones, autorización por recurso y finalidad especificadas.','X; XII–XIII; F'),
('1.3.5','Contratos de interfaz','H','Operaciones, errores y controles asociados al corte OpenAPI.','IX; E'),
('1.4.1','Incremento de identidad y acceso','H','Recorrido local de cuenta, perfil y controles de identidad comprobable.','X; XII; E–F'),
('1.4.2','Incremento de catálogo y búsqueda','H','Publicación, categorías, disponibilidad y búsqueda verificables por corte.','X; XII; E–F'),
('1.4.3','Incremento de contratación y cobros','H','Aceptación bilateral y conciliación controlada separan renta y comisión.','X; XII; E–F'),
('1.4.4','Incremento documental y avisos','H','Documentos, permisos y eventos conservan su evidencia; firma externa separada.','X; XII; E–F'),
('1.4.5','Incremento de administración y auditoría','H','Acciones privilegiadas y consulta de incidencias autorizadas por recurso.','X; XII; E–F'),
('1.5.1','Verificación de incrementos','E','Cada incremento cierra con registro de alcance, versión y pruebas.','XII; F'),
('1.5.2','Evaluación de rendimiento','E','Ensayo local y plan de carga integrada distinguen población y entorno.','XII; F'),
('1.5.3','Evaluación de recuperación','E','Restauración local y criterios de recuperación conjunta documentados.','XII–XIII; F'),
('1.5.4','Verificación de ciberseguridad','E','Permisos y escenarios de denegación conservan resultados y límites.','XII–XIII; F'),
('1.6.1','Configuración y entrega técnica','E','Entorno y automatización documentados por corte; destino AWS validado aparte.','XIII; F'),
('1.6.2','Evaluación económica','A','Flujos, VAN, TIR interpretables y sensibilidad conciliados con G/H.','XIV; H'),
('1.6.3','Preparación societaria y tributaria','A','Actividades y presupuesto identificados; no equivale a sociedad constituida.','XIV; G–H'),
('1.6.4','Informe, demostración y defensa','A','Cortes del 01-12 y 09-12 identifican entregables, evidencia y cambios.','XV–XVI; G'),
]


def main():
    people = {'H': {'nombre':'Hernán Espinoza Castillo','rol':'Arquitectura, backend y datos'},
              'A': {'nombre':'Anita Marchant Pacheco','rol':'Análisis, frontend y negocio'},
              'E': {'nombre':'Erick Silva Quezada','rol':'Seguridad, infraestructura y calidad'}}
    packages = [{'id':i,'nombre':n,'responsable':o,'aceptacion':c,'referencia':ref,
                 'limite':'Aceptación por corte y entorno; las funciones externas requieren su comprobación propia.',
                 'riesgo':'R04' if i.startswith(('1.1','1.6')) else 'R07' if i.startswith('1.4') else 'R01',
                 'revision':'Equipo del proyecto','evidencia':'Versión de artefacto y registro de revisión o prueba asociado al corte.',
                 'presupuesto':'Esfuerzo estimado de sus actividades; trabajo valorizado separado del pago.'}
                for i,n,o,c,ref in PACKAGES]
    tasks = []
    def add(i,pkg,title,owner,hours,preds='',group='Gestión y alcance',mpp=None,release=None,stage='base'):
        tasks.append({'id':i,'edt':pkg,'nombre':title,'responsable':owner,'horas':hours,
                      'predecesoras':preds.split() if preds else [],'grupo':group,
                      'mpp_ids':mpp or [],'liberacion':release,'etapa':stage,
                      'tipo':'actividad','inicio_real':None,'fin_real':None,'avance_real':None,
                      'estado':'Programación de referencia; ejecución no deducida de las fechas.',
                      'criterio':next(p['aceptacion'] for p in packages if p['id']==pkg)})
    def gate(i,title,preds,group,stage='base',fixed=None):
        tasks.append({'id':i,'edt':'1.6.4' if fixed else '1.5.1','nombre':title,'responsable':None,'horas':0,
                      'predecesoras':preds.split(),'grupo':group,'mpp_ids':[], 'liberacion':fixed,
                      'fecha_compromiso':fixed,'etapa':stage,'tipo':'hito',
                      'inicio_real':None,'fin_real':None,'avance_real':None,
                      'estado':'Hito programado; aceptación real documentada por separado.',
                      'criterio':'Cierre de las predecesoras y registro de versión y evidencia.'})
    # Gestión, análisis y diseño. Las horas son estimaciones de planificación.
    add('G01','1.1.1','Definir gobierno y acuerdo del equipo','A',8)
    add('G02','1.1.2','Delimitar alcance y descomponer EDT','A',8,'G01')
    add('G03','1.1.3','Preparar calendario y modelo de cronograma','E',12,'G01')
    add('G04','1.1.4','Identificar presupuesto y adquisiciones','A',8,'G02')
    add('G05','1.1.5','Definir riesgos y control de cambios','E',8,'G03')
    add('A01','1.2.1','Caracterizar el problema y los procesos','A',12,'G02','Análisis y diseño', [2])
    add('A02','1.2.2','Especificar requisitos funcionales','A',20,'A01','Análisis y diseño',[2])
    add('A03','1.2.3','Especificar requisitos de calidad','E',12,'A01 G05','Análisis y diseño',[2])
    add('A04','1.2.4','Modelar historias y casos de uso','A',20,'A02','Análisis y diseño',[2])
    add('A05','1.2.5','Relacionar requisitos, casos y pruebas','A',8,'A04 A03','Análisis y diseño')
    add('D01','1.3.1','Definir vistas de arquitectura empresarial','H',8,'A02 A03','Análisis y diseño',[3])
    add('D02','1.3.2','Diseñar dominio y adaptadores','H',12,'D01','Análisis y diseño',[3])
    add('D03','1.3.3','Modelar datos y restricciones geoespaciales','H',20,'D02','Análisis y diseño',[3])
    add('D04','1.3.4','Diseñar sesiones, permisos y privacidad','E',12,'D02 A03','Análisis y diseño',[3])
    add('D05','1.3.5','Especificar operaciones de interfaz','H',12,'D03 D04','Análisis y diseño',[3])
    add('L01','1.6.1','Preparar contenedores y calidad local','E',12,'G03 D02','Análisis y diseño',[4])
    # Cinco incrementos, cada uno con aceptación de integración explícita.
    add('I1H','1.4.1','Construir cuenta, perfil y control de acceso','H',32,'D05 L01','Identidad y acceso',[6,7])
    add('I1A','1.4.1','Construir pantallas de cuenta y perfil','A',24,'D05 A04','Identidad y acceso',[9])
    add('I1E','1.4.1','Definir verificación de identidad controlada','E',8,'D04','Identidad y acceso',[8])
    add('Q01','1.5.1','Verificar integración de identidad','E',8,'I1H I1A I1E','Identidad y acceso')
    gate('M01','Incremento 1 integrado','Q01','Identidad y acceso')
    add('I2H','1.4.2','Construir publicación y disponibilidad','H',24,'M01','Catálogo y búsqueda',[11])
    add('I2B','1.4.2','Construir búsqueda y cotización PostGIS','H',16,'I2H','Catálogo y búsqueda',[12])
    add('I2A','1.4.2','Construir catálogo, mapa y detalle','A',24,'M01','Catálogo y búsqueda',[13])
    add('Q02','1.5.1','Verificar catálogo y búsqueda integrada','E',8,'I2B I2A','Catálogo y búsqueda')
    gate('M02','Incremento 2 integrado','Q02','Catálogo y búsqueda')
    add('I3H','1.4.3','Construir aceptación y ocupación exclusiva','H',24,'M02','Contratación y cobros',[16])
    add('I3B','1.4.3','Construir conciliación y pagos controlados','H',12,'I3H','Contratación y cobros',[17])
    add('I3A','1.4.3','Construir recorrido de acuerdo y cobro','A',20,'M02','Contratación y cobros',[18])
    add('Q03','1.5.1','Verificar renta y comisión por separado','E',8,'I3B I3A','Contratación y cobros')
    gate('M03','Incremento 3 integrado','Q03','Contratación y cobros')
    add('I4H','1.4.4','Construir documentos, avisos y evidencias','H',24,'M03','Documentos y operación',[20,21])
    add('I4A','1.4.4','Construir vistas documentales y entrega','A',20,'M03','Documentos y operación',[22])
    add('I4E','1.4.4','Definir aceptación de firma opcional','E',8,'M03','Documentos y operación',[20])
    add('Q04','1.5.1','Verificar documentos y entrega controlada','E',8,'I4H I4A I4E','Documentos y operación')
    gate('M04','Incremento 4 integrado','Q04','Documentos y operación')
    add('I5H','1.4.5','Construir administración e incidencias','H',20,'M04','Administración y auditoría',[25,26,30])
    add('I5A','1.4.5','Construir vistas de administración','A',16,'M04','Administración y auditoría',[27,30])
    add('I5E','1.4.5','Revisar autorización y registro de auditoría','E',8,'I5H','Administración y auditoría',[30])
    add('Q05','1.5.1','Verificar incremento de administración','E',8,'I5E I5A','Administración y auditoría')
    gate('M05','Incremento 5 integrado','Q05','Administración y auditoría')
    # La transición AWS no se sitúa retrospectivamente antes de su decisión.
    add('W01','1.6.1','Conciliar diseño con decisión AWS','H',8,'D05','AWS y aceptación',[4], '2026-11-16')
    add('W02','1.6.1','Revisar adaptadores e IaC del corte AWS','E',12,'W01 L01','AWS y aceptación',[4], '2026-11-16')
    add('Q06','1.5.2','Revisar rendimiento local y plan integrado','E',8,'M05','AWS y aceptación',[31])
    add('Q07','1.5.3','Revisar recuperación local y criterios RPO/RTO','E',8,'Q06','AWS y aceptación',[31])
    add('Q08','1.5.4','Revisar permisos, regresión y hallazgos','E',8,'Q07 W02','AWS y aceptación',[31])
    add('Q09','1.5.1','Conciliar aceptación del corte académico','H',8,'Q08 M05','AWS y aceptación',[31])
    # Documentación y evaluación corren en paralelo, pero el cierre reúne ambas.
    add('F01','1.6.2','Conciliar flujos y sensibilidad financiera','A',16,'G04 A05','Informe y evaluación', [], '2026-11-16')
    add('F02','1.6.3','Definir preparación societaria y presupuesto','A',4,'G04','Informe y evaluación')
    add('R01','1.6.4','Redactar y revisar capítulos y anexos','A',24,'M03 A05','Informe y evaluación',[32])
    add('R02','1.6.4','Revisar trazabilidad de arquitectura y datos','H',8,'M05 W01','Informe y evaluación',[32])
    add('R03','1.1.3','Revisar red, recursos e hitos del plan','E',8,'Q08','Informe y evaluación',[32])
    add('R04','1.6.4','Integrar informe y evidencia de entrega','A',8,'F01 F02 R01 R02 R03 Q09','Informe y evaluación',[32])
    gate('C0','Corte académico preparado','R04','Informe y evaluación')
    gate('ENT','Entrega de proyecto e informe','C0','Entrega y defensa',fixed='2026-12-01')
    # Tramos adicionales: esfuerzo explícito, sin atribución de ejecución real.
    add('DFH','1.6.4','Estabilizar demostración técnica','H',12,'ENT','Entrega y defensa',[33],'2026-12-02','defensa')
    add('DFA','1.6.4','Preparar presentación y revisión de informe','A',12,'ENT','Entrega y defensa',[33],'2026-12-02','defensa')
    add('DFE','1.6.4','Revisar entorno de demostración y contingencias','E',12,'ENT','Entrega y defensa',[33],'2026-12-02','defensa')
    gate('DEF','Defensa de título','DFH DFA DFE','Entrega y defensa','defensa','2026-12-09')
    add('TPH','1.6.1','Verificar condiciones técnicas del piloto','H',12,'DEF','Transición comercial',[], '2026-12-10','transicion')
    add('TPA','1.6.3','Preparar formalización y captación inicial','A',12,'DEF','Transición comercial',[], '2026-12-10','transicion')
    add('TPE','1.6.1','Preparar ensayo de despliegue y proveedores','E',16,'DEF','Transición comercial',[], '2026-12-10','transicion')
    gate('COM','Inicio de fase comercial','TPH TPA TPE','Transición comercial','comercial','2027-01-01')
    for p in packages:
        p['actividades']=[t['id'] for t in tasks if t['edt']==p['id'] and t['tipo']=='actividad']
        p['horas']=sum(t['horas'] for t in tasks if t['edt']==p['id'])
    data={'version':1,'fecha_corte':'2026-11-16','nombre':'espaciGo — programa académico y transición comercial',
          'naturaleza':'Programa de referencia consolidado; no línea base histórica aprobada ni registro de horas reales.',
          'inicio':'2026-08-11','fin_base':'2026-11-30','hitos_fijos':{'ENT':'2026-12-01','DEF':'2026-12-09','COM':'2027-01-01'},
          'calendario':{'nombre':'Académico nominal 20 h','dias_semana':[0,1,2,3,4], 'horas_dia':4,'inicio_hora':'09:00','fin_hora':'13:00',
                        'excepciones':[], 'criterio':'Calendario de referencia de dedicación personal, no calendario contractual. Las excepciones de disponibilidad se registran y activan recálculo; no se presume que los feriados se hayan trabajado.'},
          'personas':people,'paquetes':packages,'actividades':tasks,'tarifa_valoracion_clp':6500,'presupuesto_valorizado_horas':960,
          'origen_mpp':{'sha256':'5140243dc56e6c7555ef9e7b0899b7e2ee11f9f12ac7b067d3116191ed5ba2a3','filas':33,'horas_asignaciones':1320},
          'evidencias_corte':[
              {'fecha':'2026-11-04','hecho':'Registro F5: 86 pruebas de primer nivel del paquete documental; F6: dos pruebas de borrador y cuatro de perfil documental.','fuente':'XII y Tabla F.3; corte técnico registrado, no aceptación productiva global.'},
              {'fecha':'2026-11-15','hecho':'Decisión de arquitectura objetivo AWS.','fuente':'context/02_arquitectura_y_diseno/ARQUITECTURA_AWS_CORTE_20261116.md'},
              {'fecha':'2026-11-16','hecho':'Evaluación económica integrada en XIV/H.','fuente':'Commit 0a1bad6 del repositorio de tesis.'}],
          'criterio_proveedores':'Los ensayos controlados del corte académico se distinguen de habilitación y prueba productiva; las tareas programadas no acreditan ejecución.',
          'estado_transicion':'Preparación propuesta del 10–31 de diciembre, con aceptación propia y comienzo comercial financiero el 01-01-2027.'}
    TARGET.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print('Paquetes',len(packages),'actividades',len(tasks),'horas',sum(t['horas'] for t in tasks))


if __name__=='__main__':main()
