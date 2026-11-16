"""Reproduce la cadena de fuentes, modelo, texto, Word y verificaciones.

La opción --render exporta PDF y páginas para la revisión visual posterior.
Una ejecución correcta no confirma entradas aún desconocidas ni aprueba el diseño.
"""
from pathlib import Path
import argparse,hashlib,json,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
def main():
 p=argparse.ArgumentParser();p.add_argument('--render',action='store_true');p.add_argument('--output-dir',default='/tmp/espacigo-economia-sapag-render');args=p.parse_args()
 scripts=['verificar_fuentes_economicas.py','ejecutar_modelo_sapag.py','actualizar_documento_ejecucion.py','build_preview.py','verificar_modelo_sapag.py','verificar_coherencia_sapag.py','verificar_liquidez_indicadores.py']
 for name in scripts:subprocess.run([sys.executable,str(ROOT/'scripts'/name)],check=True,cwd=ROOT.parent)
 doc=ROOT/'03_propuesta/build/Preparacion_economica_espaciGo.docx'
 record={'cadena':scripts,'estado_calculos':'correcto','revision_visual':'pendiente de inspección tras render','docx_sha256':hashlib.sha256(doc.read_bytes()).hexdigest()}
 if args.render:
  renderer=Path('/home/nandev/.codex/plugins/cache/openai-primary-runtime/documents/26.1112.11217/skills/documents/render_docx.py')
  out=Path(args.output_dir).resolve()
  subprocess.run([sys.executable,str(renderer),str(doc),'--output_dir',str(out),'--dpi','85','--emit_pdf'],check=True,cwd=ROOT.parent)
  pdf=doc.with_suffix('.pdf');shutil.copyfile(out/pdf.name,pdf)
  from pypdf import PdfReader
  record.update(pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),paginas_pdf=len(PdfReader(pdf).pages),directorio_revision_visual=str(out))
 (ROOT/'04_modelo_sapag/reconstruccion_actual.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':main()
