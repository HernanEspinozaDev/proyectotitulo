from pathlib import Path
import json,sys,os,shutil,zipfile,tempfile
from lxml import etree as E
root=Path(__file__).resolve().parents[2]
p=root/'preparacion_economica_anita/03_propuesta'
templates=p/'templates'
templates.mkdir(exist_ok=True)
shutil.copyfile(root/'tesis_final/templates/reference-tihi84.docx',templates/'reference.docx')
profile=json.loads((root/'tesis_final/templates/style-profile-inacap.json').read_text())
profile['template']['file']='templates/reference.docx'
(templates/'style-profile.json').write_text(json.dumps(profile,ensure_ascii=False,indent=2))
m={'version':1,'id':'preparacion_economia_anita','metadata':{'title':'Preparación económica de espaciGo','subtitle':'Documento de preparación para revisión','authors':['Espinoza Castillo, Hernán','Marchant Pacheco, Anita','Silva Quezada, Erick'],'lang':'es-CL','date':'16 de noviembre de 2026'},'sections':['capitulo_xiv_borrador.md','anexo_h_tablas_fuente.md'],'appendices':[],'template':'templates/reference.docx','style_profile':'templates/style-profile.json','output':'Preparacion_economica_espaciGo.docx','toc':{'enabled':False}}
(p/'document.json').write_text(json.dumps(m,ensure_ascii=False,indent=2))
sys.path.insert(0,str(root/'docskill'))
os.environ.setdefault('DOCSKILL_PANDOC',str(root/'docskill/.tools/pandoc/bin/pandoc'))
from docskill.api import DocSkillProject
project=DocSkillProject.open(p)
v=project.validate()
assert v.success,v.to_dict()
result=project.build()
assert result.success,result.to_dict()
path=p/'build/Preparacion_economica_espaciGo.docx'
w='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
with zipfile.ZipFile(path) as z:
 payload={name:z.read(name) for name in z.namelist()}
doc=E.fromstring(payload['word/document.xml'])
for table_index,table in enumerate(doc.iter(w+'tbl')):
 pr=table.find(w+'tblPr')
 if pr is None:pr=E.SubElement(table,w+'tblPr')
 borders=pr.find(w+'tblBorders')
 if borders is not None:pr.remove(borders)
 borders=E.SubElement(pr,w+'tblBorders')
 for edge in ('top','left','bottom','right','insideH','insideV'):
  E.SubElement(borders,w+edge,{w+'val':'single',w+'sz':'4',w+'color':'000000'})
 previous=table.getprevious()
 if previous is not None and previous.tag==w+'p':
  pp=previous.find(w+'pPr')
  if pp is None:pp=E.SubElement(previous,w+'pPr')
  if pp.find(w+'keepNext') is None:E.SubElement(pp,w+'keepNext')
 for tr in table.findall(w+'tr'):
  rp=tr.find(w+'trPr')
  if rp is None:rp=E.SubElement(tr,w+'trPr')
  if rp.find(w+'cantSplit') is None:E.SubElement(rp,w+'cantSplit')
 count=len(table.find(w+'tr').findall(w+'tc'))
 if table_index==4:
  weights=[.65,.35]
 elif table_index==5:
  weights=[.20,.20,.30,.30]
 elif table_index<4:
  weights=([.40,.20,.25,.15] if count==4 else [.30]+[.70/(count-1)]*(count-1))
 else:
  weights=[.08]+[.92/(count-1)]*(count-1) if count>1 else [1]
 widths=[round(8560*x) for x in weights]
 grid=table.find(w+'tblGrid')
 if grid is not None:
  for node,width in zip(grid.findall(w+'gridCol'),widths):node.set(w+'w',str(width))
 for tr in table.findall(w+'tr'):
  for cell,width in zip(tr.findall(w+'tc'),widths):
   cp=cell.find(w+'tcPr')
   if cp is None:cp=E.SubElement(cell,w+'tcPr')
   cw=cp.find(w+'tcW')
   if cw is None:cw=E.SubElement(cp,w+'tcW')
   cw.set(w+'type','dxa');cw.set(w+'w',str(width))
 if table_index<2:
  paras=list(table.iter(w+'p'))
  for para in paras[:-1]:
   pp=para.find(w+'pPr')
   if pp is None:pp=E.SubElement(para,w+'pPr')
   if pp.find(w+'keepNext') is None:E.SubElement(pp,w+'keepNext')
 row=table.find(w+'tr')
 if row is not None:
  rp=row.find(w+'trPr')
  if rp is None:rp=E.SubElement(row,w+'trPr')
  E.SubElement(rp,w+'tblHeader')
  for para in row.iter(w+'p'):
   pp=para.find(w+'pPr')
   if pp is None:pp=E.SubElement(para,w+'pPr')
   if pp.find(w+'keepNext') is None:E.SubElement(pp,w+'keepNext')
  for cell in row.findall(w+'tc'):
   cp=cell.find(w+'tcPr')
   if cp is None:cp=E.SubElement(cell,w+'tcPr')
   E.SubElement(cp,w+'shd',{w+'fill':'D9E2F3'})
 for run in table.iter(w+'r'):
  props=run.find(w+'rPr')
  if props is None:props=E.SubElement(run,w+'rPr')
  size=props.find(w+'sz')
  if size is None:size=E.SubElement(props,w+'sz')
  size.set(w+'val','18')
for para in doc.iter(w+'p'):
 pr=para.find(w+'pPr')
 if pr is None:continue
 style=pr.find(w+'pStyle')
 if style is not None and any(style.get(w+'val','').startswith(x) for x in ('Ttulo','Heading')):
  num=pr.find(w+'numPr')
  if num is None:num=E.SubElement(pr,w+'numPr')
  for child in list(num):num.remove(child)
  E.SubElement(num,w+'numId',{w+'val':'0'})
  if style.get(w+'val') in ('Ttulo1','Heading1'):
   E.SubElement(pr,w+'pageBreakBefore')
payload['word/document.xml']=E.tostring(doc,xml_declaration=True,encoding='UTF-8',standalone=True)
with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
 for name,blob in payload.items():z.writestr(name,blob)
print(path)
print('Tablas Word',len(list(doc.iter(w+'tbl'))))
