#!/usr/bin/env python3
"""Construye, presenta, renderiza y sincroniza una entrega local de ES2."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from datetime import datetime, timezone

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
ES2 = ROOT.parent
ENGINE = ROOT.parent / 'docskill'
BUILD = ROOT / 'build'
DOCX = BUILD / 'Informe_Desarrollo_e_Implementacion_espaciGo.docx'
PDF = BUILD / 'Informe_Desarrollo_e_Implementacion_espaciGo.pdf'
ASSEMBLED = BUILD / 'assembled.md'
MANIFEST = BUILD / 'manifest.json'
VALIDATION = BUILD / 'validation.md'
DIAGNOSTICS = BUILD / 'diagnostics.json'
DELIVERY = ES2 / 'Informe_Desarrollo_e_Implementacion_espaciGo_ES2'
ROOT_MANIFEST = DELIVERY.with_name(DELIVERY.name + '_manifest.json')
SOFFICE = Path('/home/nandev/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/libreoffice-headless/libreoffice/program/soffice')
sys.path.insert(0, str(ENGINE))
os.environ.setdefault('DOCSKILL_PANDOC', str(ENGINE / '.tools/pandoc/bin/pandoc'))
from docskill import DocSkillProject

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024*1024), b''): h.update(chunk)
    return h.hexdigest()

def artifact(path, relative):
    return {'path': relative, 'sha256': digest(path), 'size_bytes': path.stat().st_size}

def run(label, command, env=None):
    print(f'=== {label} ===', flush=True)
    result = subprocess.run(command, cwd=ROOT, env=env, text=True, capture_output=True)
    if result.stdout: print(result.stdout.rstrip())
    if result.returncode:
        if result.stderr: print(result.stderr.rstrip(), file=sys.stderr)
        raise RuntimeError(f'{label} terminó con código {result.returncode}')
    return result

def run_pipeline():
    if not SOFFICE.is_file(): raise RuntimeError(f'No se encontró LibreOffice del runtime documental: {SOFFICE}')
    run('0. Figuras BPMN verticales reproducibles', [sys.executable, str(ROOT/'scripts/render_bpmn_vertical.py')])
    run('1. Reconstrucción del Anexo B desde las migraciones locales', [sys.executable, str(ROOT/'scripts/build_anexo_b_perfect.py')])
    project = DocSkillProject.open(ROOT)
    print('=== 2. Validación DocSkill ===', flush=True)
    validation = project.validate()
    if not validation.success: raise RuntimeError(json.dumps(validation.to_dict(), ensure_ascii=False, indent=2))
    build = project.build()
    if not build.success: raise RuntimeError(json.dumps(build.to_dict(), ensure_ascii=False, indent=2))
    if not MANIFEST.is_file() or not DOCX.is_file(): raise RuntimeError('DocSkill no produjo DOCX y manifest.')
    base_manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    base_docx = artifact(DOCX, 'build/Informe_Desarrollo_e_Implementacion_espaciGo.docx')
    print(f'DOCX base: {base_docx["size_bytes"]} bytes, SHA-256 {base_docx["sha256"]}')
    run('3. Presentación OOXML reproducible de portada, saltos y tablas', [sys.executable, str(ROOT/'scripts/postprocess_docx_layout.py')])
    env = os.environ.copy(); env['ES2_SOFFICE'] = str(SOFFICE); env['ES2_UNO_PYTHON'] = sys.executable
    ver = subprocess.run([str(SOFFICE), '--version'], capture_output=True, text=True, check=True, env=env).stdout.strip()
    toc_result = run('4. TOC con paginación real, actualización del campo y renderizado PDF aislado', [sys.executable, str(ROOT/'scripts/update_docskill_toc.py')], env=env)
    toc_match = __import__('re').search(r'Índice TOC con (\d+) títulos y páginas verificadas; renderizado estable en (\d+) iteración', toc_result.stdout)
    if not toc_match: raise RuntimeError('La actualización del TOC no informó una verificación estable.')
    if not all(p.is_file() and p.stat().st_size > 0 for p in (DOCX, PDF, ASSEMBLED)):
        raise RuntimeError('Falta una salida generada no vacía.')

    # Conserva literalmente el manifest emitido por DocSkill como fase base y
    # expone, por separado, los artefactos finales ya posprocesados.
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    output = manifest.setdefault('output', {})
    output['sha256'] = digest(DOCX)
    output['size_bytes'] = DOCX.stat().st_size
    manifest['phases'] = {
        'docskill_base': {'status':'success', 'artifact':base_docx, 'manifest_output_sha256':base_manifest.get('output',{}).get('sha256')},
        'layout_postprocess': {'status':'success', 'script':'scripts/postprocess_docx_layout.py', 'script_sha256':digest(ROOT/'scripts/postprocess_docx_layout.py')},
        'bpmn_portrait': {'status':'success', 'script':'scripts/render_bpmn_vertical.py', 'script_sha256':digest(ROOT/'scripts/render_bpmn_vertical.py'), 'page_orientation':'portrait', 'image_width_in':5.7, 'model_format':'BPMN 2.0 XML and DI'},
        'field_update_and_pdf_render': {'status':'success', 'script':'scripts/update_docskill_toc.py', 'script_sha256':digest(ROOT/'scripts/update_docskill_toc.py'), 'renderer':ver}
    }
    manifest['final_artifacts'] = {
        'docx':artifact(DOCX, 'build/Informe_Desarrollo_e_Implementacion_espaciGo.docx'),
        'pdf':artifact(PDF, 'build/Informe_Desarrollo_e_Implementacion_espaciGo.pdf'),
        'markdown':artifact(ASSEMBLED, 'build/assembled.md'),
        'validation':artifact(VALIDATION, 'build/validation.md'),
        'diagnostics':artifact(DIAGNOSTICS, 'build/diagnostics.json')
    }
    manifest.setdefault('toc', {}).update({'cached_result_entries':int(toc_match.group(1)), 'render_iterations':int(toc_match.group(2)), 'page_mapping_stable':True, 'field_instruction_preserved':True})
    validation_copy = DELIVERY.with_name(DELIVERY.name + '_validation.md')
    diagnostics_copy = DELIVERY.with_name(DELIVERY.name + '_diagnostics.json')
    manifest['local_delivery'] = {'markdown':str(DELIVERY.with_suffix('.md').relative_to(ES2)), 'docx':str(DELIVERY.with_suffix('.docx').relative_to(ES2)), 'pdf':str(DELIVERY.with_suffix('.pdf').relative_to(ES2)), 'validation':str(validation_copy.relative_to(ES2)), 'diagnostics':str(diagnostics_copy.relative_to(ES2)), 'manifest':str(ROOT_MANIFEST.relative_to(ES2))}
    manifest['updated_at'] = datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    # Volver a leer el JSON y comparar con archivos ya guardados.
    saved = json.loads(MANIFEST.read_text(encoding='utf-8'))
    if saved['output']['sha256'] != digest(DOCX) or saved['final_artifacts']['pdf']['sha256'] != digest(PDF):
        raise RuntimeError('Los hashes del manifest no coinciden tras guardarlo.')

    # Sincronización local, todos los archivos salen de la misma ejecución.
    shutil.copyfile(ASSEMBLED, DELIVERY.with_suffix('.md'))
    shutil.copyfile(DOCX, DELIVERY.with_suffix('.docx'))
    shutil.copyfile(PDF, DELIVERY.with_suffix('.pdf'))
    shutil.copyfile(VALIDATION, validation_copy)
    shutil.copyfile(DIAGNOSTICS, diagnostics_copy)
    shutil.copyfile(MANIFEST, ROOT_MANIFEST)
    for source, target in [(ASSEMBLED, DELIVERY.with_suffix('.md')), (DOCX, DELIVERY.with_suffix('.docx')), (PDF, DELIVERY.with_suffix('.pdf')), (VALIDATION, validation_copy), (DIAGNOSTICS, diagnostics_copy)]:
        if digest(source) != digest(target): raise RuntimeError(f'Copia de entrega difiere del build: {target.name}')
    print('Entrega local sincronizada con los hashes del manifest:')
    for path in (DELIVERY.with_suffix('.md'), DELIVERY.with_suffix('.docx'), DELIVERY.with_suffix('.pdf'), validation_copy, diagnostics_copy, ROOT_MANIFEST): print(f'  {path}: {path.stat().st_size} bytes')
    print(f'Hash DOCX final: {digest(DOCX)}')
    print(f'Hash PDF final:  {digest(PDF)}')
    return 0

if __name__ == '__main__':
    try: raise SystemExit(run_pipeline())
    except Exception as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        raise SystemExit(1)
