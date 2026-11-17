"""Reconstruye la preparación adoptada con DocSkill y auditorías."""
from pathlib import Path
import argparse,subprocess,sys,json,shutil,hashlib
ROOT=Path(__file__).resolve().parents[1]
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--render',action='store_true');parser.add_argument('--output-dir',default='/tmp/espacigo-escenario-adoptado');args=parser.parse_args()
 sequence=['verificar_fuentes_economicas.py','escenario_adoptado.py','actualizar_escenario_adoptado.py','build_preview.py','verificar_escenario_adoptado.py']
 for name in sequence:subprocess.run([sys.executable,str(ROOT/'scripts'/name)],check=True,cwd=ROOT.parent)
 doc=ROOT/'03_propuesta/build/Preparacion_economica_espaciGo.docx'
 record=dict(cadena=sequence,modelo='06_escenario_adoptado/parametros.json',docx_sha256=hashlib.sha256(doc.read_bytes()).hexdigest(),revision_visual='pendiente tras render')
 if args.render:
  renderer='/home/nandev/.codex/plugins/cache/openai-primary-runtime/documents/26.1112.11217/skills/documents/render_docx.py'
  output=Path(args.output_dir).resolve();subprocess.run([sys.executable,renderer,str(doc),'--output_dir',str(output),'--dpi','85','--emit_pdf'],check=True,cwd=ROOT.parent)
  pdf=doc.with_suffix('.pdf');shutil.copyfile(output/pdf.name,pdf)
  from pypdf import PdfReader
  record.update(pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),paginas_pdf=len(PdfReader(pdf).pages),directorio_revision_visual=str(output))
 (ROOT/'06_escenario_adoptado/reconstruccion.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':main()
