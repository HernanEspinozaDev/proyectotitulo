"""Impide publicar rutas de trabajo o enlaces al repositorio en la tesis."""
from pathlib import Path
import json,re,zipfile
from lxml import etree as E
ROOT=Path(__file__).resolve().parents[1]
PATTERNS=[r'/home/',r'\btesis_final/',r'\bcontext/',r'\bassets/',r'\bplanning/',r'\bdiagramas_src/',r'\b(?:[\w.-]+/)+[\w.-]+\.(?:md|py|json|ya?ml|csv|docx|xlsx|puml|mmd)\b',r'github\.com/HernanEspinozaDev/(?:espaciGo|espacigo-aws)',r'\bDocSkill\b',r'\brender_planificacion\.py\b',r'\bCronograma_espaciGo_Project\.xml\b']
PATTERNS += [r'\b(?:aws-emulator|Mailpit|aws-main|local-emulator|espacigo-aws|s3storage|documents3|Dockerfile)\b', r'\bcmd/api\b', r'\binternal/adapters/postgres\b', r'\brepositorio(?:s)?\b', r'\bcommits?\b', r'\b(?:3dc1c18|b1b38d1|8d33dcf|cc2fdc3|93b59c8|4e26d52b57d9687c4b6b7a778e89dbbb5be855e5)\b']
def check(text,origin):
    assert not re.search(r'\bV[0-9]{1,6}\b',text),(origin,'código de migración visible')
    for pattern in PATTERNS:
        hit=re.search(pattern,text,re.I)
        assert not hit,(origin,hit.group() if hit else '')
manifest=json.loads((ROOT/'document.json').read_text())
for name in manifest['sections']:
    source=(ROOT/name).read_text()
    source=re.sub(r'!\[[^\]]*\]\([^)]*\)(?:\{[^}]*\})?','',source)
    check(source,name)
with zipfile.ZipFile(ROOT/'build/Tesis_Final_espaciGo.docx') as z:
    for name in ['word/document.xml','word/footnotes.xml','word/endnotes.xml']:
        if name in z.namelist():
            root=E.fromstring(z.read(name));check(' '.join(root.itertext()),name)
from pypdf import PdfReader
reader=PdfReader(ROOT/'build/Tesis_Final_espaciGo.pdf')
for i,page in enumerate(reader.pages):
    check(page.extract_text() or '',f'PDF página {i+1}')
    for ref in page.get('/Annots',[]):
        action=ref.get_object().get('/A')
        if action:check(str(action.get('/URI','')),f'enlace PDF página {i+1}')
result={'estado':'verificado','secciones_y_anexos':len(manifest['sections']),'paginas_pdf':len(reader.pages),'rutas_de_trabajo_visibles':0,'enlaces_repositorio_proyecto':0,'rutas_imagenes_fuente':'conservadas fuera del texto visible','endpoints_api':'conservados como especificación técnica'}
target=ROOT/'context/01_auditorias_y_rubricas/verificacion_sin_rutas_de_trabajo.json';target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False))
