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
# Reutilizar el juicio metodológico documentado, sin atribuir sus puntajes a PMI.
p=T/'sections/06-capitulo-vi.md';old=p.read_text();start=old.index('**Tabla 5**');end=old.index('#### 6.1.3.')
selection=old[start:end].strip().replace('[@pmbok7]','[@pmbok6]')
selection=selection.replace('El total suma cada valoración multiplicada por su ponderación [@pmbok6].','El total suma cada valoración multiplicada por su ponderación. Las ponderaciones y valoraciones corresponden al juicio técnico del proyecto; PMI no prescribe estos puntajes.')
risks=[
('R01','Doble reserva concurrente','3 × 5 = 15; alta','H','Solapamiento de solicitudes','Exclusión temporal e idempotencia; verificar concurrencia antes de aceptar el flujo.'),
('R02','Degradación del proveedor de pagos','2 × 5 = 10; media','H','Respuesta tardía o conciliación discrepante','Reintentos idempotentes, conciliación y reversos; mantener la habilitación externa condicionada.'),
('R03','Exposición de datos privados','2 × 5 = 10; media','E','Acceso indebido o permisos restaurados incorrectos','Autorización por recurso y finalidad, pruebas negativas y verificación tras restauración.'),
('R04','Incumplimiento de entrega','3 × 4 = 12; alta','E','Desplazamiento de una actividad crítica','Revisión semanal y diaria del tramo crítico; congelar alcance del corte y registrar impacto.'),
('R05','Inadecuación de evidencia contractual','1 × 4 = 4; baja','A','Requisito de firma o contenido no satisfecho','Revisar modalidades y documentos; separar aceptación bilateral y firma opcional.'),
('R06','Disponibilidad personal inferior al calendario','3 × 4 = 12; alta','A','Ausencia o dedicación semanal inferior a 20 h','Registrar excepciones y recalcular; reasignar solo con competencias y capacidad verificadas.'),
('R07','Diferencia entre entorno local y entorno objetivo','2 × 4 = 8; media','E','Servicio o configuración incompatible','Revisar artefactos y preparar ensayo independiente; no inferir aceptación cloud del emulador.'),
('R08','Volumen comercial insuficiente','2 × 4 = 8; media','A','Pagos procesados inferiores al umbral económico','Contrastar demanda y sensibilidad del Capítulo XIV; escalonar gasto según caja disponible.')]
vi='''# CAPÍTULO VI: Metodología de trabajo

## 6. Metodología de trabajo

### 6.1. Metodología y Desarrollo de la solución

#### 6.1.1. Gobierno y ciclo de vida

La gestión se fundamenta en prácticas adaptadas de la Guía del PMBOK, sexta edición de 2017 [@pmbok6, pp. 19, 23, 28]. La guía organiza procesos de inicio, planificación, ejecución, monitoreo/control y cierre; estos procesos se aplican durante el proyecto y no equivalen a fases consecutivas de construcción del software. El desarrollo adopta un ciclo iterativo e incremental, con análisis, diseño, construcción y verificación por incremento.

El enfoque híbrido combina entregables y fechas académicas definidas con refinamiento técnico progresivo. El registro distingue especificación del producto, evidencia local e integración en el entorno objetivo. La programación consolidada al 16 de noviembre de 2026 constituye una referencia de trabajo; no se presenta como una línea base aprobada en agosto ni como reconstrucción de horas efectivamente trabajadas.

#### 6.1.2. Selección del enfoque

La matriz compara el ajuste de tres enfoques a las restricciones de este proyecto. La aplicación utiliza controles de alcance y recursos proporcionados a un equipo de tres integrantes.

'''+selection+'\n\n'+'''#### 6.1.3. Fases e incrementos

La Figura 3 representa las actividades que se repiten y revisan en el ciclo de construcción. La secuencia se concreta en cinco incrementos: identidad y cuenta; catálogo y búsqueda; aceptación y cobros; documentos y avisos; administración y auditoría. Cada incremento integra componentes y una revisión identificada Q01–Q05 antes del hito M01–M05. Las revisiones locales de rendimiento y recuperación pueden ejecutarse sobre componentes disponibles; la aceptación del sistema integrado conserva su evidencia propia.

'''+figure('3','Ciclo de construcción y revisión por incremento','fig04_ciclo_vida_objetivo',width='13cm',note='Elaboración propia. El ciclo se aplica a cada incremento; los procesos de gestión acompañan su desarrollo [@pmbok6].')+'''#### 6.1.4. Gestión del alcance y diccionario EDT

El alcance del Capítulo V, la EDT y su diccionario organizan la referencia de alcance del proyecto [@pmbok6, pp. 156, 161–162]. La Figura 4 conserva seis ramas y 28 paquetes de entregables. La actualización precisa sus nombres, distingue el acuerdo de gobierno de la constitución societaria y separa la preparación comercial de su realización efectiva.

'''+figure('4','Estructura de desglose del trabajo de espaciGo','edt_paquetes',note='Elaboración propia. Los 28 identificadores se conservan y vinculan el diccionario G.2 con las actividades G.3.')+'''El Anexo G.2 desarrolla una ficha para cada paquete: responsable de coordinación, producto, criterio de aceptación, actividades, esfuerzo, recursos, límites, riesgo y referencia de evidencia. El responsable del paquete coordina su aceptación; las actividades pueden asignarse a otro integrante según su especialidad. El modelo separa entregables de la EDT y tareas del cronograma. Ninguna ficha se considera aceptada por la sola existencia de una fecha programada.

#### 6.1.5. Gestión de riesgos

La evaluación utiliza probabilidad de 1 (muy baja) a 5 (muy alta) e impacto de 1 (menor) a 5 (crítico). El producto de ambos valores define prioridad baja entre 1 y 4, media entre 5 y 10 y alta entre 11 y 25. La escala es ordinal y no representa probabilidades estadísticas. El Anexo G.9 agrega dueño, disparador y seguimiento. El responsable revisa los riesgos por corte y cuando cambia su disparador [@pmbok6, pp. 417, 419, 437, 442].

'''+figure('5','Mapa de probabilidad e impacto de los riesgos','mapa_riesgos',width='13cm',note='Elaboración propia a partir de la Tabla 6. Las posiciones muestran valoraciones cualitativas del proyecto.')+table('6','Registro resumido de riesgos',['ID','Riesgo','Evaluación','Respuesta'],[(k,title,score,response) for k,title,score,owner,trigger,response in risks])+'''#### 6.1.6. Gobierno, integración y control

El propósito académico consiste en entregar el informe institucional, el repositorio identificable, la demostración del corte y sus evidencias de ingeniería. El equipo decide los ajustes técnicos dentro del alcance documentado; la evaluación y cualquier cambio de fecha institucional corresponden a la autoridad académica. La ficha de gobierno del Anexo G no sustituye un acta institucional firmada. El acuerdo de funcionamiento del proyecto y la futura constitución de la empresa tienen finalidades diferentes.

La adaptación integra las diez áreas de gestión: integración mediante control de versiones y cambios; alcance mediante EDT y requisitos; cronograma mediante dependencias y recursos; costos mediante conciliación de G/H; calidad mediante criterios del Anexo F; recursos mediante responsables y calendario; comunicaciones e interesados mediante G.9; riesgos mediante la Tabla 6; y adquisiciones mediante los criterios de habilitación y presupuesto. Esta aplicación evita atribuir cumplimiento integral o certificación PMI al proyecto.

Una solicitud de cambio registra origen, motivo, entregables afectados, impacto en horas, fechas, caja y riesgos, decisión y versión. El responsable del frente analiza el impacto y el equipo resuelve el ajuste técnico; una fecha académica no se modifica sin la autorización correspondiente. El Capítulo XV conserva la comparación de versiones. El plan de comunicaciones de G.9 define destinatarios y frecuencia, sin atribuir comunicaciones o aprobaciones aún no realizadas.

### 6.2. Duración y cronograma

#### 6.2.1. Calendario, fechas y estimación

El desarrollo se programa desde el 11 de agosto hasta el 30 de noviembre de 2026. La entrega corresponde al 1 de diciembre, la defensa al 9 de diciembre y el inicio de la fase comercial al 1 de enero de 2027. El tramo del 2 al 9 de diciembre se reserva para preparación de defensa; la transición posterior se distingue de la entrega académica.

Cada integrante dispone de veinte horas semanales. El calendario nominal distribuye cuatro horas diarias de lunes a viernes, de 09:00 a 13:00, como unidad de programación de dedicación personal. No representa un horario contractual ni acredita trabajo en feriados. No se registran excepciones de disponibilidad en esta referencia; cualquier excepción efectiva requiere incorporarse y recalcular antes de usar el programa como compromiso de ejecución. Entre el 11 de agosto y el 30 de noviembre existen ochenta jornadas nominales: 320 horas por persona y 960 del equipo.

El esfuerzo se estima por juicio técnico y desglose de entregables, en bloques de cuatro horas. La duración de una actividad corresponde al esfuerzo dividido por cuatro cuando una persona concentra su ejecución; el tiempo calendario incluye fines de semana, liberaciones y esperas. Las fechas previas al corte son posiciones del programa reconstruido y no fechas reales verificadas. Los campos reales permanecen sin atribución hasta contar con registro por actividad.

#### 6.2.2. Programación, dependencias y recursos

El registro maestro contiene 63 nodos, con actividades y hitos de duración cero. La red utiliza relaciones fin a comienzo. La revisión de arquitectura puede comenzar con el alcance preliminar y se concilia después con requisitos; la documentación progresa durante los incrementos. Las compuertas reúnen frontend, backend y revisión. Las tareas W01/W02 conservan una liberación el 16 de noviembre para conciliar la decisión AWS documentada en el corte, sin trasladarla ficticiamente a agosto.

El cálculo determina fechas tempranas y tardías y holgura; después reproduce la secuencia de cada persona mediante vínculos de disponibilidad. El Anexo G distingue predecesoras lógicas y de recurso, verifica ausencia de ciclos y comprueba que ninguna persona supera cuatro horas diarias o veinte semanales. La selección de esta secuencia factible no demuestra que sea la única ni la óptima [@pmbok6, pp. 210–215].

'''+figure('6','Cronograma maestro del desarrollo, defensa y transición','gantt_maestro')+'''#### 6.2.3. Ruta crítica y límites de factibilidad

El cierre del desarrollo se calcula para el 30 de noviembre de 2026 a las 13:00. La entrega se mantiene el 1 de diciembre. La holgura disponible en jornadas completas antes de esa entrega es cero. El tramo crítico del cierre reúne W01, W02, Q08, las ramas Q09 y R03, R04 y el hito C0. El Anexo G.5 presenta la red y la holgura de todas las actividades académicas. Las fechas de defensa e inicio comercial se tratan como hitos fijos; no se utilizan para inflar la holgura del trabajo académico.

La factibilidad es condicionada: una jornada adicional en W01 o W02 desplaza el cierre al 1 de diciembre y compromete la preparación previa a la entrega. La capacidad sin asignar no constituye reserva temporal en la ruta crítica y la reserva presupuestaria no compra automáticamente disponibilidad especializada. El control prioriza ese tramo, limita nuevas funciones y recalcula ante una ausencia o cambio. Las pruebas externas no terminadas se conservan como condiciones de habilitación; sus resultados no se sustituyen con un hito de calendario.

### 6.3. Equipo de trabajo

#### 6.3.1. Responsabilidad y revisión

El equipo está formado por Hernán Espinoza Castillo, Anita Marchant Pacheco y Erick Silva Quezada. La siguiente matriz sintetiza responsabilidad de coordinación; G.2/G.3 conserva la asignación por paquete y actividad.

'''+table('7','Asignación de responsabilidades del equipo',['Frente','Hernán Espinoza Castillo','Anita Marchant Pacheco','Erick Silva Quezada'],[
('Gobierno, alcance y costos','C','A/R','C'),('Análisis y requisitos','C','A/R','R'),('Arquitectura, backend y datos','A/R','C','R'),('Frontend y experiencia','C','A/R','C'),('Calidad, seguridad y cronograma','R','C','A/R'),('Infraestructura y despliegue','R','C','A/R'),('Economía y preparación legal','C','A/R','C'),('Informe y defensa','R','A/R','R')],note='Elaboración propia. R: ejecuta; A: coordina la conformidad del frente; C: consulta. Cada fila tiene una sola A. La aceptación académica corresponde a la autoridad institucional.')+'''#### 6.3.2. Esfuerzo y seguimiento

La programación asigna 228 horas académicas a Hernán Espinoza, 240 a Anita Marchant y 164 a Erick Silva: 632 en total. La preparación de defensa asigna doce horas a cada integrante, y la transición agrega doce, doce y dieciséis, respectivamente. El total del programa es 708 horas estimadas. El Anexo G.6 verifica carga y distribución semanal. Estas cifras no se presentan como horas reales ni como remuneraciones.

El registro de seguimiento identifica actividad, fecha de estado, esfuerzo real, esfuerzo restante, evidencia, revisión y fecha prevista de cierre. El avance se reconoce por entregable comprobado; una fecha pasada no acredita terminación. Sin línea base aprobada y medidas reales comparables, SPI, CPI y variaciones de ejecución se informan como no calculables. Los indicadores operativos del Capítulo XI mantienen su finalidad propia.

### 6.4. Plan de recursos

El trabajo utiliza equipos personales compartidos, repositorio, herramientas de desarrollo y entornos de ensayo. La capacidad nominal académica de 960 horas deja 328 horas sin asignar en esa etapa. El presupuesto de trabajo valorizado conserva 960 horas a CLP 6.500: CLP 6.240.000. Al asignar expresamente 76 horas a defensa y transición, el programa completo consume 708 horas valorizadas en CLP 4.602.000 y conserva una reserva presupuestaria de 252 horas, CLP 1.638.000. La capacidad libre académica y la reserva de todo el programa tienen bases temporales diferentes.

La valorización mide recursos del proyecto y se separa de pagos al equipo y del flujo de caja comercial. El Capítulo XIV y el Anexo H mantienen la inversión monetaria y los costos comerciales desde enero de 2027. La conciliación no modifica el flujo por convertir horas disponibles en egresos ficticios.

La planificación de adquisiciones identifica los servicios previstos, responsable, partida y prueba de aceptación en G.9. La arquitectura AWS y sus adaptadores se revisan como artefactos; la configuración regional, contratación, despliegue y aceptación externa siguen los controles del Capítulo XIII. La modalidad opcional de firma y los pagos requieren validación independiente de sus proveedores antes de habilitación.
'''
vi=vi.replace('![](assets/figuras/fig04_ciclo_vida_objetivo.png){width=13cm}', '![](assets/figuras/fig04_ciclo_vida_objetivo.png){height=11cm}')
p.write_text(vi)
# Anexo completo, generado por secciones y tablas pequeñas para lectura en formato vertical.
g='''# ANEXO G: CARTA GANTT MAESTRA Y PROGRAMACIÓN DETALLADA DEL PROYECTO

## G.1. Alcance, fuentes y calendario

El anexo operacionaliza el Capítulo VI y aplica prácticas adaptadas de la sexta edición de la Guía del PMBOK [@pmbok6]. El corte de planificación es el 16 de noviembre de 2026. El programa reconstruido establece una referencia; no acredita una línea base histórica aprobada, horas reales ni ejecución de proveedores. El MPP recibido se conserva como fuente de inventario, sin modificar el original. Los ID originales se relacionan con las actividades de G.3.

El calendario nominal considera cuatro horas diarias de lunes a viernes y veinte semanales por persona. El registro de excepciones está vacío en esta referencia y debe actualizarse ante una disponibilidad distinta; no se presume trabajo histórico en feriados. Una jornada de duración equivale a cuatro horas de esfuerzo de su responsable, y las fechas abarcan también esperas entre actividades. Las relaciones son fin a comienzo; una predecesora de recurso representa el orden de uso de una persona y se distingue de la necesidad lógica del entregable.

'''+table('G.1','Fechas rectoras y condiciones de cierre',['Hito','Fecha','Condición'],[
('Inicio de desarrollo','11-08-2026','Inicio de referencia confirmado para programación.'),('C0: corte preparado',fmt(BY['C0']['fin']),'Informe, código y evidencia identificados para entrega.'),('ENT: entrega','01-12-2026','Versión entregable y limitaciones registradas; no acredita aceptación docente.'),('DEF: defensa','09-12-2026','Demostración y presentación con diferencias respecto de ENT.'),('COM: fase comercial','01-01-2027','Inicio del Año 1 económico; operación condicionada a habilitación técnica y legal.')])+'''## G.2. Diccionario de los 28 paquetes de la EDT

Cada ficha identifica el producto del paquete, su coordinación y las tareas que lo materializan. La revisión corresponde al equipo con contraste del criterio; la evaluación institucional conserva su autoridad propia. Los recursos comunes comprenden equipo personal compartido, repositorio y entorno pertinente. La evidencia consiste en versión de artefacto y registro de revisión o prueba del corte. Estos campos describen el criterio de aceptación y no afirman su realización futura.

'''
for pk in M['paquetes']:
    g+=f"**EDT {pk['id']}. {pk['nombre']}**\n\n"
    g+=f"Responsable de coordinación: {M['personas'][pk['responsable']]['nombre']}. Entregable: {pk['nombre'].lower()}. Criterio de aceptación: {pk['aceptacion']}\n\n"
    g+=f"Actividades: {', '.join(pk['actividades'])}. Esfuerzo: {pk['horas']} h; valorización: {clp(pk['horas']*6500)}, diferenciada del pago. Referencia de producto y evidencia: {pk['referencia']}. Recursos: equipo personal, repositorio y entorno del componente. Riesgo principal: {pk['riesgo']}. Límite: {pk['limite']}\n\n"
g+='''La revisión de nombres conserva los 28 identificadores: el paquete 1.1.1 expresa gobierno del proyecto, y 1.6.3 expresa preparación legal, sin afirmar constitución societaria realizada. Los hitos de compuerta reúnen evidencia y tienen esfuerzo cero; las tareas asignadas a cada paquete evitan sumar horas nuevamente por el hito.

## G.3. Registro de actividades y correspondencia de fuentes

Los ID son estables. La asignación H corresponde a Hernán Espinoza Castillo; A, a Anita Marchant Pacheco; E, a Erick Silva Quezada. La columna MPP conserva el ID de origen cuando existe. Un guion identifica actividad nueva o desglose sin correspondencia directa. La relación puede ser uno a varios; la fuente aporta inventario, no fechas ni esfuerzo verificado.

'''
g+='''Los hitos de evaluación 14 y 23 del MPP se conservan como antecedentes, sin trasladar sus fechas discordantes a compromisos nuevos no confirmados. El hito 28 se sustituye por ENT del 1 de diciembre; el 33 se separa en ENT y DEF del 9 de diciembre. Los hitos M01–M05 agregan compuertas técnicas de incremento y no se presentan como las evaluaciones docentes históricas.

'''
for n in range(0,len(C['actividades']),12):
    rows=C['actividades'][n:n+12]
    g+=table(f'G.3.{n//12+1}','Actividades, entregables y origen: parte '+str(n//12+1),['ID / EDT','Actividad','Responsable / h','MPP'],[(r['id']+' / '+r['edt'],r['nombre'],(r['responsable'] or 'Hito')+' / '+str(r['horas']),', '.join(map(str,r['mpp_ids'])) or '—') for r in rows])
g+='''El criterio de aceptación de cada actividad corresponde al entregable de su paquete G.2 y al criterio específico del registro maestro. Las tareas de revisión Q06/Q07 y W01/W02 verifican evidencia disponible y preparan comprobaciones del entorno objetivo; no se interpretan como ensayos externos aprobados. Los campos de inicio real, fin real y avance real no se rellenan a partir de la programación.

## G.4. Vistas de la Gantt

La Figura 6 presenta el resumen en el cuerpo. Las tres vistas siguientes contienen los 63 nodos una sola vez, en el orden estable del registro; la escala temporal es común. El orden de las filas no implica precedencia: los vínculos y fechas de G.5 la determinan. Las barras de resumen representan intervalos de cobertura y no añaden horas a las actividades.

'''
for n in range(1,4):g+=figure(f'G.{n}',f'Cronograma detallado: panel {n} de 3',f'gantt_detalle_{n}')
g+='''## G.5. Dependencias, holguras y ruta crítica

La red se ordena topológicamente y se programa con el calendario y liberaciones. La revisión incorpora el orden de uso de cada persona como relaciones de recurso y comprueba que no existe solapamiento de sus asignaciones. El CPM se calcula para los antecesores de C0: la programación lógica y la nivelada alcanzan el 30 de noviembre. La igualdad de fecha no elimina la necesidad de controlar capacidad. Las holguras corresponden a jornadas nominales de cuatro horas y no a días corridos.

'''+figure('G.4','Tramo crítico de cierre académico','red_critica_planificacion',note='Elaboración propia a partir de las relaciones calculadas. Dos ramas de holgura cero convergen en la integración R04.')
base=[r for r in C['actividades'] if r['id'] in C['cpm_nivelado']['filas']]
for n in range(0,len(base),12):
    rows=base[n:n+12]
    g+=table(f'G.5.{n//12+1}','Fechas y vínculos de la red: parte '+str(n//12+1),['ID','Inicio / fin','Predecesoras lógicas; de recurso','Holgura'],[(r['id'],fmt(r['inicio'])+' / '+fmt(r['fin']),(', '.join(r['predecesoras']) or '—')+'; R: '+(', '.join(r['predecesoras_recursos']) or '—'),str(r['holgura_red_nivelada'])+' j') for r in rows])
g+='''El archivo de cálculo conserva, además, ES, EF, LS y LF por ID en índices de jornada: cero corresponde al 11 de agosto; un fin de índice n corresponde a las 13:00 de la jornada anterior a n. Esta convención permite reproducir holguras sin confundir fechas de inicio y fin. Los hitos ENT, DEF y COM utilizan fechas compromiso separadas del CPM del desarrollo.

Las liberaciones de W01 y W02 consideran la disponibilidad de la decisión AWS desde el corte del 16 de noviembre; F01 utiliza el mismo corte de integración económica. Los hitos no se anticipan por terminar antes sus predecesoras. La preparación de defensa se programa del 2 al 4 de diciembre; la transición, del 10 al 15, con frontera comercial el 1 de enero. Las disponibilidades posteriores no compensan retrospectivamente atrasos del desarrollo.

La reserva temporal previa a ENT es cero jornadas completas. Un aumento de cuatro horas en W01 desplaza en una jornada el camino crítico y lleva el cierre al 1 de diciembre. Por ello, el plan exige revisión diaria de ese tramo, congelamiento de funciones y registro del impacto antes de comprometer cambios. La reserva monetaria y la capacidad libre de otras fechas o especialidades no se presentan como holgura de esa red.

## G.6. Recursos, esfuerzo y capacidad

'''+table('G.6','Capacidad nominal y asignación de esfuerzo',['Integrante','Base / capacidad','Defensa / transición','Total'],[(M['personas'][k]['nombre'],str(C['horas_base_por_persona'][k])+' / 320 h',str(sum(r['horas'] for r in C['actividades'] if r['responsable']==k and r['etapa']=='defensa'))+' / '+str(sum(r['horas'] for r in C['actividades'] if r['responsable']==k and r['etapa']=='transicion'))+' h',str(C['horas_totales_por_persona'][k])+' h') for k in M['personas']])+'''El desarrollo dispone de 960 horas nominales y asigna 632; quedan 328 horas sin asignar en ese tramo. La comprobación diaria y semanal del archivo de cálculo no identifica sobrecargas: cada actividad ocupa cuatro horas por jornada de su responsable y ninguna semana supera veinte. La comprobación no acredita disponibilidad efectiva futura. La actualización registra ausencias y dedicación real antes de recalcular.

El esfuerzo de 708 horas del programa completo incluye 36 de defensa y 40 de transición. Las 252 horas de reserva presupuestaria pertenecen al techo global de 960 horas valorizadas; no deben sumarse a la capacidad libre académica ni confundirse con horas realizadas. Los equipos son personales compartidos; su disponibilidad no implica compra inicial ni aporte exclusivo de activos.

## G.7. Seguimiento, aceptación y cambios

'''+table('G.7','Registro mínimo de seguimiento y reglas',['Campo o control','Regla de aplicación'],[
('Fecha de estado','Registrar el corte de medición; no utilizar la fecha del sistema como evidencia de término.'),('ID, versión y entorno','Relacionar paquete, actividad, commit o documento, entorno y registro de ensayo.'),('Real y restante','Registrar inicio/fin efectivos, horas reales y estimación restante; conservar sin dato cuando no existe evidencia.'),('Aceptación','Revisión conforme, conforme dentro del alcance del ensayo, requiere ajuste o no comprobado; identificar revisor y fecha.'),('Avance de entregables','Reconocer terminación comprobada del criterio; presentar cobertura parcial con sus límites.'),('Indicadores','Comparar fecha prevista y compromiso; SPI/CPI requieren línea base y medidas reales comparables, ausentes en este corte.'),('Cambio','Identificar solicitante/origen, motivo, impacto en alcance, horas, fechas, caja y riesgos, decisión y versión.'),('Escalamiento','Un cambio que afecta entrega o defensa se eleva a revisión académica; no se da por aprobado al editar el archivo.')])+'''Las revisiones de integración M01–M05 requieren componentes relacionados y ensayo Q01–Q05. El hito C0 identifica una versión reproducible del informe y repositorio, resultados con sus límites y lista de condiciones pendientes. La aceptación del corte sintético o local no sustituye aceptación de todas las categorías ni de proveedores. El Anexo F mantiene la fuente de resultados realmente observados; las actas futuras se completan cuando ocurren.

## G.8. Conciliación económica y temporal

'''+table('G.8','Puente del cronograma con la valoración económica',['Componente','Horas','Valor a CLP 6.500/h'],[
('Desarrollo académico',632,clp(632*6500)),('Preparación de defensa',36,clp(36*6500)),('Transición preoperativa',40,clp(40*6500)),('Actividades programadas',708,clp(708*6500)),('Reserva presupuestaria',252,clp(252*6500)),('Presupuesto valorizado',960,clp(6240000))])+'''Las filas de actividades y reserva concilian el presupuesto, sin duplicar los subtotales de etapas. La cifra original de 1.320 horas del MPP corresponde a asignaciones de un recurso sin nombre y no concilia con el trabajo de tarea registrado en cero; no se adopta como esfuerzo medido. La ventana anterior de 360 horas hasta diciembre se reemplaza por la separación explícita de etapas.

La valoración de trabajo se diferencia del efectivo de preparación y lanzamiento y de las remuneraciones comerciales. La conciliación conserva el presupuesto valorizado de CLP 6.240.000 y no modifica por sí sola la caja, VAN, TIR o recuperación del Capítulo XIV. El Año 0 comprende preparación y el Año 1 comienza el 1 de enero de 2027; la entrega del 1 de diciembre no inicia ingresos comerciales ficticios.

## G.9. Riesgos, comunicaciones, interesados y adquisiciones

'''+table('G.9.1','Seguimiento operativo de riesgos',['ID / dueño','Disparador','Control y seguimiento'],[(k+' / '+owner,trigger,response+' Revisión semanal y ante cambio; sin cierre acreditado por calendario.') for k,title,score,owner,trigger,response in risks])+table('G.9.2','Plan de comunicaciones',['Destinatario','Contenido / responsable','Frecuencia y canal'],[
('Equipo','Avance, impedimentos y riesgos / responsable del frente','Semanal; diaria en tramo crítico. Registro versionado y coordinación interna.'),('Profesora y evaluadores','Informe, dudas y cambios de fecha / coordinación académica del equipo','Por hito o cambio que afecta evaluación; canal institucional disponible.'),('Usuarios y publicantes','Criterios, recorrido y observaciones / análisis y negocio','Por sesión de validación con consentimiento y registro de entorno.'),('Proveedores','Condiciones, pruebas y habilitación / responsable técnico','Antes de activar servicio y ante incidencias; canal oficial del proveedor.')],note='Elaboración propia. La matriz define comunicaciones a realizar; no acredita mensajes enviados ni respuestas recibidas.')+table('G.9.3','Registro de interesados y participación',['Interesado','Interés / influencia','Expectativa y estrategia'],[
('Equipo fundador','Alto / alta','Entrega verificable y dedicación viable; revisión cruzada por frente.'),('Profesora y comisión','Alto / alta académica','Cumplimiento de plantilla, fechas y evidencia; entregar cortes y consultar impactos institucionales.'),('Publicantes y usuarios','Alto / media sobre producto','Claridad de disponibilidad, precios y condiciones; validar recorridos y registrar necesidades por categoría.'),('Proveedores tecnológicos','Medio / alta técnica','Integración y condiciones de servicio; validar cada dependencia antes de activarla.'),('Organismos reguladores','Interés normativo / alta regulatoria','Cumplimiento tributario y de datos; revisar requisitos y conservar decisiones documentadas.')])+table('G.9.4','Plan de adquisiciones y aceptación de servicios',['Servicio / responsable','Presupuesto y condición','Evidencia exigida'],[
('Infraestructura objetivo / E','Partidas cloud de XIV/H; configuración y región según XIII','Revisión de IaC y ensayo de acceso, despliegue y recuperación en entorno habilitado.'),('Mercado Pago / H','Cargo según modelo económico; proveedor previsto sin activación acreditada','Acreditación, conciliación, separación de cobros y reembolso.'),('Firma opcional / H','Modalidad y costo por uso separados; SimpleFirma prevista','Prueba por emisión/firmante, documento y reversos.'),('Preparación legal / A','Incluida en CLP 1.200.000 de preparación y lanzamiento','Trámites, comprobantes y condiciones para operación; no afirmar constitución realizada.'),('Captación / A','CLP 350.000 mensuales, separados del lanzamiento','Registro de gasto, conversión y decisión de continuidad según caja.')])+'''## G.10. Cierre y transferencia

El cierre académico conserva informe y PDF, manifiesto de fuentes, commit del código, migraciones, ensayos, limitaciones, demostración y registro de cambios. La entrega ENT fija su corte; la versión de defensa identifica mejoras posteriores sin reescribir la entrega. El control comprueba accesibilidad y correspondencia entre repositorio, anexos y demostración.

La transferencia posterior revisa condiciones legales, proveedores, despliegue y recuperación; no declara clientes, ingresos ni servicios habilitados por el transcurso del calendario. Los pendientes técnicos se transfieren con dueño y criterio del Anexo F. El inicio comercial de enero de 2027 constituye la frontera del escenario económico y requiere que la habilitación efectiva se evalúe con sus evidencias.

El modelo editable se conserva en `tesis_final/assets/diagramas_src/cronograma_espacigo.json`; el código de cálculo y figuras reside en `tesis_final/scripts/calcular_cronograma.py` y `render_planificacion.py`. Las tablas interoperables y el intercambio `Cronograma_espaciGo_Project.xml` se conservan en la preparación de planificación. El XML es un formato de intercambio para Project; el MPP de origen no se reemplaza por un archivo de otra naturaleza.
'''
(T/'appendices/g-carta-gantt-detallada.md').write_text(g)
xv='''# CAPÍTULO XV: Ajustes del Cronograma

## 15. Ajustes del Cronograma

### 15.1. Revisión de Carta Gantt o desarrollo de fases

La revisión conserva el inventario útil de la carta original y reconstruye calendario, responsables y dependencias según el Capítulo VI y el Anexo G. El archivo de origen sitúa actividades en 2009–2010, no identifica al recurso y conserva un hito final desconectado. Sus 1.320 horas de asignación no se consideran horas reales, y su ruta almacenada de 117 días no acredita el cumplimiento de los hitos académicos actuales.

La programación de referencia se inicia el 11 de agosto de 2026, con entrega el 1 de diciembre y defensa el 9. La reconstrucción explicita 28 paquetes y 63 nodos, con responsables y calendario de veinte horas semanales por persona. El primer ensayo de secuenciación concentra verificaciones y documentos al final y alcanza el 14 de diciembre, por lo que incumple la entrega. La corrección permite diseño preliminar tras delimitar alcance, documentación progresiva y ensayos locales sobre incrementos disponibles. No reduce el esfuerzo de 708 horas ni cambia la fecha institucional para aparentar cumplimiento.

La nueva secuencia alcanza C0 el 30 de noviembre y conserva cero jornadas completas de margen antes de ENT. La revisión condiciona su uso a disponibilidad efectiva y ejecución del trabajo restante: las fechas reconstruidas anteriores al corte no constituyen evidencia de avance real. El programa no se presenta como línea base aprobada en agosto ni se calcula una variación histórica contra una base inexistente.

### 15.2. Registro integrado de ajustes

El cambio de infraestructura se trata como actualización de diseño: las actividades W01/W02 concilian artefactos y criterios del corte AWS desde el 16 de noviembre. La documentación histórica mantiene su entorno y resultados de origen. La inclusión de esas revisiones no afirma un despliegue productivo ni el cierre de las pruebas de proveedores.

La corrección de calendario separa desarrollo académico, preparación de defensa y transición preoperativa. El puente económico conserva 960 horas de presupuesto valorizado: 708 asignadas y 252 de reserva; las actividades posteriores a la entrega se identifican expresamente. No se duplican esas horas como remuneraciones o compra de equipos. Los ingresos comerciales se evalúan desde el 1 de enero de 2027.

El registro de configuración relaciona ID del cambio, motivo, actividades, evidencia, impacto y versión del informe. La reconstrucción inicial, su ensayo rechazado y el cálculo corregido permanecen como archivos de auditoría; no equivalen a actas de aprobación docente. Las nuevas decisiones se registran antes de sustituir versiones y se contrastan con las restricciones de alcance y fecha.

### 15.3. Seguimiento y cierre por corte

La revisión semanal recoge fecha de estado, horas reales, esfuerzo restante, evidencia y fecha prevista por actividad. El tramo crítico W01–W02–Q08–Q09/R03–R04 requiere revisión diaria y escalamiento ante desvíos. Un aumento de cuatro horas en una actividad de ese tramo consume la jornada siguiente y compromete la preparación previa a la entrega. El control limita funciones nuevas y registra su impacto; la reserva presupuestaria no se interpreta como holgura de calendario.

La conformidad se registra por criterio y entorno: conforme, conforme dentro del alcance del ensayo, requiere ajuste o no comprobado. Sin evidencia por actividad, el avance y los indicadores de valor ganado permanecen no calculables. Los resultados del Capítulo XII y el Anexo F no se transforman automáticamente en porcentajes de terminación del cronograma.

La entrega del 1 de diciembre conserva su versión de informe, código y evidencia. La defensa del 9 identifica ajustes posteriores y su demostración. El cierre transfiere limitaciones, riesgos y condiciones de habilitación al trabajo preoperativo sin atribuir aceptaciones futuras; el Anexo G.10 establece la lista de control. El inicio comercial de enero corresponde al estudio económico y no sustituye una decisión técnica de puesta en servicio.
'''
(T/'sections/15-capitulo-xv.md').write_text(xv)
print('Integrados VI, XV y Anexo G: 28 fichas, registro completo, red y control.')
