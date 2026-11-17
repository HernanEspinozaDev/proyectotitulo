"""Aplicación editorial; conserva cálculos y nombres físicos del diccionario DDL."""
from pathlib import Path
import re,json
ROOT=Path(__file__).resolve().parents[1];T=ROOT/'tesis_final';P=ROOT/'revision_editorial_revisor_20261117'
manifest=json.loads((T/'document.json').read_text());changes={}
def save(p,s):
 old=p.read_text()
 if old!=s:changes[str(p.relative_to(ROOT))]=True;p.write_text(s)
# Registro de aplicación inicial: no repetir sobre la narrativa ya corregida.
if 'El punto de entrada de la API reside' not in (T/'sections/09-capitulo-ix.md').read_text():
    raise SystemExit('La aplicación editorial ya está registrada; ejecutar verificar_revision.py para auditar la versión actual.')
# Primero, equivalencias conceptuales en cada capítulo y después en los anexos.
for rel in manifest['sections']:
 p=T/rel;s=p.read_text()
 s=s.replace('Local development uses aws-emulator.','Local development uses an AWS-compatible emulation environment.')
 s=s.replace('the V000075 local snapshot','the local development schema snapshot')
 replacements={
 'y concentra el desarrollo verificable en el repositorio espacigo-aws':'y organiza el desarrollo verificable de la plataforma',
 'El repositorio espacigo-aws declara':'La configuración de infraestructura de la plataforma declara',
 'El repositorio espacigo-aws, corte 3dc1c18 del 16 de noviembre de 2026, incorpora migraciones hasta V000098.':'El corte técnico de infraestructura del 16 de noviembre de 2026 incorpora la evolución versionada del esquema relacional.',
 'en espacigo-aws, corte 3dc1c18 del 16 de noviembre':'en el corte técnico de infraestructura del 16 de noviembre',
 'del repositorio espacigo-aws, corte 3dc1c18 del 16 de noviembre de 2026':'del corte técnico de la plataforma del 16 de noviembre de 2026',
 'El corte 3dc1c18':'El corte técnico verificado de infraestructura',
 'arquitectura del repositorio':'arquitectura de la plataforma',
 'estructura del repositorio':'estructura de componentes de la plataforma',
 'el repositorio identificable':'el código fuente verificable de la plataforma',
 'repositorio inmutable':'almacén inmutable',
 'aws-emulator':'entorno local de emulación compatible con AWS',
 'Mailpit':'servidor SMTP local de pruebas',
 'La configuración aws-main':'La configuración de infraestructura principal en AWS',
 'local-emulator y aws-main':'local y principal en AWS',
 'Receta `Dockerfile`':'Definición de contenedor',
 'Adaptadores s3storage y documents3':'Adaptadores de almacenamiento de objetos y documentos',
 'Los cambios se identifican por commit':'Los cambios se identifican mediante el control de versiones',
 'el registro identifica el commit':'el registro identifica la revisión técnica verificada',
 'commit del código':'versión verificada del código',
 'commit o documento':'versión de código o documento',
 'La migración V000009 de espaciGo declara':'El esquema relacional de espaciGo declara',
 'las figuras 10 y 11 describen persistencia':'las figuras 11 y 12 describen persistencia',
 'El registro local `outbox_evento_local`':'El registro transaccional de eventos de salida (patrón Transactional Outbox)',
 }
 for a,b in replacements.items():s=s.replace(a,b)
 # Suprimir códigos de creación de fichas; no cambian columnas, claves ni SQL.
 s=re.sub(r'^- \*\*Migración de creación:\*\*[^\n]*\n','',s,flags=re.M)
 s=re.sub(r',?\s*commit\s+`?[a-f0-9]{7,40}`?','',s,flags=re.I)
 s=re.sub(r'\b(Backend|Frontend)\s+`[a-f0-9]{7,40}`\.',lambda m:'Revisión verificada del '+m[1].lower()+'.',s)
 s=s.replace('V53 y V54','las revisiones versionadas de contratación y cobros').replace('V37 y V80','las revisiones de verificación de reputación')
 s=s.replace('V1–V61','las migraciones versionadas del esquema relacional')
 s=s.replace('captura V000075','captura del esquema local de desarrollo').replace('captura local V000075','captura local del esquema de desarrollo')
 s=re.sub(r'\bV\d{1,6}\b','la revisión versionada del esquema',s)
 s=re.sub(r'\bcorte [a-f0-9]{7,40}\b','corte técnico verificado',s)
 s=re.sub(r'\brepositorios\b','adaptadores de persistencia',s)
 s=re.sub(r'\brepositorio\b','sistema de control de versiones',s)
 save(p,s)
# Capítulo IX: describir capas y responsabilidades, no el árbol del código.
p=T/'sections/09-capitulo-ix.md';s=p.read_text();a=s.index('El punto de entrada');b=s.index('\n\nEl diseño asigna',a)
s=s[:a]+'La capa de entrada HTTP recibe las solicitudes de la API y aplica los controles de sesión y autorización. Los módulos internos de dominio agrupan las responsabilidades de espacios, ocupación, reservas, contratación y verificación documental. Los adaptadores de persistencia PostgreSQL y almacenamiento de objetos S3 conectan esas reglas con sus dependencias técnicas. Esta organización delimita responsabilidades y permite verificar componentes con dependencias controladas.'+s[b:];save(p,s)
# Capítulo X: nombres conceptuales, sin convertir tablas físicas en prosa del cuerpo.
p=T/'sections/10-capitulo-x.md';s=p.read_text().replace('La copia de trabajo del ADR','La especificación de diseño ratificada').replace('Su incorporación al catálogo físico se registra por separado en la revisión versionada del esquema.','Su incorporación al catálogo físico se documenta mediante las actualizaciones versionadas del esquema.')
s=s.replace('La restricción `EXCLUDE USING gist` compara la igualdad de `espacio_id` y el solapamiento de `intervalo`','La restricción de exclusión compara la identidad del espacio y el solapamiento del intervalo temporal')
s=s.replace('en `public.ocupacion` la columna `intervalo` de tipo `tstzrange`','un intervalo de ocupación de tipo `tstzrange`')
s=s.replace('informa  Este contrato se guarda sin firma electrónica de las partes .','informa «Este contrato se guarda sin firma electrónica de las partes».')
s=s.replace('una capa HTTP de entrada `cmd/api`','una capa HTTP de entrada')
s=s.replace('cmd/api','la capa de entrada HTTP de la API').replace('s3storage y documents3','adaptadores de objetos y documentos S3')
s=s.replace('en un endpoint HTTPS propio','mediante un endpoint HTTPS propio');save(p,s)
# VI: códigos técnicos definidos en el anexo, prosa conceptual en el cuerpo.
p=T/'sections/06-capitulo-vi.md';s=p.read_text()
s=s.replace('una revisión identificada Q01–Q05 antes del hito M01–M05','una verificación de integración antes de su compuerta de aceptación')
s=s.replace('Las tareas W01/W02 conservan una liberación el 16 de noviembre para conciliar la decisión AWS documentada en el corte, sin trasladarla ficticiamente a agosto.','Las actividades de adecuación de infraestructura AWS se programan desde el 16 de noviembre, fecha del corte técnico que sustenta su revisión.')
s=s.replace('La selección de esta secuencia factible no demuestra que sea la única ni la óptima','La programación constituye una secuencia factible nivelada dentro de las restricciones académicas')
s=s.replace('El tramo crítico del cierre reúne W01, W02, Q08, las ramas Q09 y R03, R04 y el hito C0.','El tramo crítico reúne la adecuación de infraestructura AWS, la revisión de permisos y regresión, las revisiones paralelas de aceptación y cronograma, la integración del informe y el hito de cierre del desarrollo.')
s=s.replace('una jornada adicional en W01 o W02','una jornada adicional en las actividades críticas de adecuación de infraestructura')
s=s.replace('Estas cifras no se presentan como horas reales ni como remuneraciones.','Estas cifras corresponden a la estimación técnica de esfuerzo académico y preoperativo del programa.')
s=s.replace('no se utilizan para inflar la holgura del trabajo académico','se distinguen del cálculo de holgura del trabajo académico');save(p,s)
# XII y XIII: cada código de cronograma conserva explicación en G.
p=T/'sections/12-capitulo-xii.md';s=p.read_text();a=s.index('Las actividades Q01–Q05');s=s[:a]+'''Las verificaciones de integración se organizan por incremento; las revisiones de rendimiento y recuperación contrastan la evidencia local con los criterios del ensayo integrado. La revisión final reúne regresión, permisos y aceptación del corte académico. El Anexo G identifica las actividades correspondientes y sus dependencias. Las fechas representan programación; los resultados efectivamente comprobados se conservan en este capítulo y en el Anexo F. La aceptación de la entrega académica identifica sus límites y conserva las verificaciones externas pendientes de ejecución.
''';save(p,s)
p=T/'sections/13-capitulo-xiii.md';s=p.read_text();a=s.index('La programación W01/W02');s=s[:a]+'''La planificación del Anexo G relaciona esta secuencia con las actividades de adecuación del diseño y revisión de infraestructura AWS. La transición preoperativa identifica responsables de preparación técnica, legal y de proveedores. La frontera comercial del 1 de enero de 2027 corresponde al estudio económico. La puesta en servicio efectiva exige acreditar los controles de este capítulo mediante sus evidencias de aceptación.
''';save(p,s)
# XV: explicación vigente del programa, sin la historia del archivo de origen.
p=T/'sections/15-capitulo-xv.md';save(p,'''# CAPÍTULO XV: Ajustes del Cronograma

## 15. Ajustes del Cronograma

### 15.1. Revisión de Carta Gantt o desarrollo de fases

La planificación estructura los 28 paquetes de la EDT en 54 actividades y nueve hitos, con responsables, dependencias y nivelación de recursos. El programa integra el desarrollo académico entre el 11 de agosto y el 30 de noviembre de 2026, la entrega del 1 de diciembre, la preparación de defensa y la transición preoperativa. El Capítulo VI presenta la síntesis y el Anexo G desarrolla la programación detallada.

La dedicación de veinte horas semanales por integrante permite programar análisis, diseño, construcción y verificación por incremento. La documentación se desarrolla de manera progresiva y las verificaciones locales se coordinan con la disponibilidad de los componentes. La estimación asigna 632 horas al desarrollo académico, 36 a preparación de defensa y 40 a transición preoperativa, para un total de 708 horas.

El hito de cierre del desarrollo se sitúa el 30 de noviembre. El margen previo a la entrega equivale a cero jornadas completas, por lo que el control prioriza la disponibilidad de los responsables y la revisión del esfuerzo restante en las actividades críticas. Las fechas constituyen la programación de referencia; el seguimiento registra separadamente la ejecución observada y sus evidencias.

### 15.2. Registro integrado de ajustes

La adecuación de infraestructura AWS incorpora la revisión de arquitectura y de sus componentes técnicos desde el 16 de noviembre. Su aceptación distingue la evidencia de desarrollo local de los ensayos del entorno objetivo. La preparación técnica de proveedores y despliegue conserva los criterios de los capítulos XII y XIII.

La revisión integra alcance, secuencia, disponibilidad y presupuesto de esfuerzo. El techo de trabajo valorizado corresponde a 960 horas: 708 asignadas y 252 de reserva presupuestaria. La valoración se concilia con el Anexo H y se diferencia de desembolsos y remuneraciones comerciales. La operación económica se inicia el 1 de enero de 2027.

Cada ajuste registra su motivo, los entregables afectados, el impacto en esfuerzo, fechas, costos y riesgos, la decisión y la versión de aplicación. Los cambios que afectan fechas institucionales se someten a la revisión académica correspondiente. La versión de entrega y la versión de defensa conservan sus propios registros de configuración.

### 15.3. Seguimiento y cierre por corte

La revisión semanal recoge fecha de estado, esfuerzo real y restante, evidencia y fecha prevista por actividad. El tramo crítico comprende adecuación de infraestructura, regresión y permisos, aceptación, revisión del cronograma e integración del informe. Ese tramo requiere revisión diaria y escalamiento ante desvíos. Una jornada adicional compromete la preparación previa a la entrega y activa la revisión de alcance y disponibilidad.

La conformidad se registra por criterio y entorno: conforme, conforme dentro del alcance del ensayo, requiere ajuste o no comprobado. El cálculo de indicadores de valor ganado requiere una línea base y medidas reales comparables. Los resultados del Capítulo XII y el Anexo F sustentan la revisión de entregables dentro de sus respectivos alcances.

La entrega del 1 de diciembre identifica informe, código y evidencia. La defensa del 9 de diciembre incorpora los ajustes posteriores y la demostración correspondiente. El cierre transfiere limitaciones, riesgos y condiciones de habilitación a la preparación comercial, según el Anexo G.10. El inicio económico de enero se coordina con la decisión técnica de puesta en servicio y los controles de aceptación.
''')
# DDL: encabezar la ficha históricamente sin alterar el nombre físico documentado.
p=T/'appendices/d-diccionario-de-datos-ddl.md';s=p.read_text();s=s.replace('### B.022 Tabla `public.gcp06_test_access_batch_audit`','### B.022 Auditoría histórica por lotes de control de acceso\n\nLa ficha documenta la tabla física histórica `public.gcp06_test_access_batch_audit`. Su denominación se conserva para interpretar el DDL de referencia; registra auditorías por lotes de pruebas de control de acceso y no identifica la infraestructura cloud vigente.')
s=s.replace('La versión de creación más alta registrada en las fichas es la revisión versionada del esquema. ','').replace('se declaran en la revisión versionada del esquema','se declaran en las revisiones de verificación documental')
s=s.replace('con la captura la revisión versionada del esquema','con la captura del esquema de desarrollo')
s=s.replace('Las migraciones del sistema de control de versiones AWS todavía contienen identificadores heredados como gcp06_test_access_batch_audit, cli_gcp06 y literales de proveedor gcs.','El DDL histórico conserva identificadores y literales de proveedores anteriores en las fichas de referencia.')
s=s.replace('conserva el corte histórico reconstruido','documenta el corte histórico reconstruido');save(p,s)
# Economía: cambiar el orden argumental, manteniendo todos los resultados numéricos.
lead='Los umbrales calculados de actividad con VAN positivo al 12 % son 392 pagos mensuales sin asignaciones a fundadores y 793 con una asignación de CLP 200.000 mensuales por integrante, con ticket promedio de CLP 50.000. Estos volúmenes constituyen metas analíticas de sostenibilidad bajo el presupuesto evaluado y requieren validar los costos de una operación de mayor escala.'
p=T/'sections/11-capitulo-xi.md';s=p.read_text().replace('Evaluación económica integrada: VAN base negativo al 12 % con 16 pagos mensuales. Se calculan aportes, sensibilidad y metas de volumen.','Umbrales de VAN positivo al 12 %: 392 pagos mensuales sin asignaciones y 793 con CLP 200.000 por fundador. El piloto técnico de ocho espacios y 16 pagos mensuales requiere aportes; se evalúan sensibilidad y financiamiento.');save(p,s)
p=T/'sections/14-capitulo-xiv.md';s=p.read_text();s=s.replace('El escenario base establece un inventario','La referencia de marcha blanca técnica controlada establece un inventario',1)
a=s.index('La proyección base de dieciséis pagos mensuales',s.index('### 14.8.'))
s=s[:a]+lead+'\n\nLa referencia inicial de ocho espacios y dieciséis pagos mensuales corresponde al escenario proyectado de marcha blanca técnica controlada, destinado a organizar el piloto y evaluar sus necesidades de financiamiento; se distingue de la meta comercial en régimen. Esta referencia genera CLP 288.000 de ingreso neto anual frente a CLP 6.168.036,24 de costo operativo en el primer año. Su VAN sin deuda es −CLP 20.053.400,45 al 12 % y requiere aportes durante el horizonte evaluado. La alternativa con préstamo modifica el calendario de financiamiento y mantiene la necesidad de cubrir el déficit de actividad.\n\nEl proyecto prioriza validar captación, aumentar volumen, revisar costos y controlar caja antes de habilitar asignaciones. La evaluación de desarrollo, reposición y cierre complementa el análisis financiero y el presupuesto se actualiza con registros de actividad y alcance tecnológico.\n';save(p,s)
p=T/'sections/16-capitulo-xvi.md';s=p.read_text();s=re.sub(r'^- \*\*OE5\..*$', '- **OE5. Operación y factibilidad.** '+lead+' La referencia inicial de marcha blanca técnica controlada comprende ocho espacios y 16 pagos mensuales. El Capítulo XIV y el Anexo H muestran que ese piloto requiere aportes y presenta un VAN sin deuda de −CLP 20.053.400,45; sus resultados delimitan las necesidades de financiamiento y la distancia respecto de las metas comerciales.',s,flags=re.M);save(p,s)
# Las fuentes editables de figuras también adoptan nombres conceptuales.
p=T/'assets/diagramas_src/fig09_componentes_aws.puml';s=p.read_text().replace('cmd/api\\n','Entrada HTTP de la API\\n').replace('s3storage y documents3\\n','Persistencia de objetos y documentos S3\\n').replace('Mailpit en desarrollo','Servidor SMTP local de pruebas').replace('aws-emulator\\nS3 local por HTTPS','Entorno local compatible con AWS\\nAlmacenamiento S3 por HTTPS');save(p,s)
(P/'archivos_corregidos.json').write_text(json.dumps(list(changes),ensure_ascii=False,indent=2)+'\n')
print('Archivos corregidos:',len(changes))
