#!/usr/bin/env python3
"""Entrada local al motor DocSkill existente. No ejecuta operaciones Git."""
import argparse
import json
import os
from pathlib import Path
import sys
import subprocess

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
ENGINE = ROOT.parent / 'docskill'
sys.path.insert(0, str(ENGINE))
os.environ.setdefault('DOCSKILL_PANDOC', str(ENGINE/'.tools/pandoc/bin/pandoc'))
from docskill import DocSkillProject


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('accion', choices=['inspeccionar', 'validar', 'construir'])
    args = parser.parse_args()
    project = DocSkillProject.open(ROOT)
    if args.accion == 'inspeccionar':
        result = project.inspect()
        ok = result.valid
    elif args.accion == 'validar':
        result = project.validate()
        ok = result.success
    else:
        # La salida de entrega requiere también reglas de tablas, BPMN, índice,
        # renderizado y hashes; un build base perdería esas correcciones visuales.
        return subprocess.run([sys.executable, str(ROOT/'scripts/build_full_report.py')], cwd=ROOT).returncode
    print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
