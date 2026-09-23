"""Renderiza un DOCX con Word 365 y PyMuPDF sin alterar el original.

Ejemplo:
    python Informes/herramientas/render_docx_windows.py entrada.docx --out salida
"""

import argparse
from pathlib import Path
import shutil
import subprocess
import sys


def renderizar(origen: Path, salida: Path, timeout: int, dpi: int) -> int:
    if sys.platform != "win32":
        raise RuntimeError("Este renderizador requiere Windows y Microsoft Word")
    if not origen.is_file() or origen.suffix.lower() != ".docx":
        raise FileNotFoundError(f"DOCX no encontrado: {origen}")
    try:
        import pymupdf
    except ImportError as error:
        raise RuntimeError("PyMuPDF no está disponible para PDF → PNG") from error

    salida.mkdir(parents=True, exist_ok=True)
    copia = salida / "copia.docx"
    pdf = salida / "documento.pdf"
    pid_file = salida / "word.pid"
    registro = salida / "exportacion.log"
    if origen.resolve() == copia.resolve():
        raise ValueError("La salida debe ser distinta del DOCX original")
    shutil.copy2(origen, copia)
    pdf.unlink(missing_ok=True)
    pid_file.unlink(missing_ok=True)

    comando = [
        "powershell.exe", "-NoProfile", "-STA", "-ExecutionPolicy", "Bypass",
        "-File", str(Path(__file__).with_name("exportar_pdf_word.ps1")),
        "-Source", str(copia), "-Pdf", str(pdf), "-PidFile", str(pid_file),
    ]
    with registro.open("w", encoding="utf-8") as archivo:
        proceso = subprocess.Popen(comando, stdout=archivo, stderr=subprocess.STDOUT)
        try:
            codigo = proceso.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            if pid_file.exists():
                pid = pid_file.read_text(encoding="utf-8").strip()
                if pid.isdecimal() and int(pid) > 0:
                    subprocess.run(
                        ["taskkill", "/PID", pid, "/T", "/F"],
                        capture_output=True, text=True, timeout=10, check=False,
                    )
            proceso.kill()
            proceso.wait(timeout=10)
            raise TimeoutError(f"Exportación Word excedió {timeout} s; revisar {registro}")

    if codigo != 0 or not pdf.is_file() or pdf.stat().st_size == 0:
        raise RuntimeError(f"Word no generó un PDF válido; revisar {registro}")

    paginas = salida / "paginas"
    paginas.mkdir(exist_ok=True)
    with pymupdf.open(pdf) as documento:
        if len(documento) == 0:
            raise RuntimeError(f"PDF sin páginas: {pdf}")
        for anterior in paginas.glob("page-*.png"):
            anterior.unlink()
        escala = dpi / 72
        for numero, pagina in enumerate(documento, 1):
            archivo = paginas / f"page-{numero:03d}.png"
            pagina.get_pixmap(matrix=pymupdf.Matrix(escala, escala), alpha=False).save(archivo)
        print(f"PDF: {pdf} ({len(documento)} páginas)")
        print(f"PNG: {paginas}")
        print(f"Registro: {registro}")
        return len(documento)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("docx", type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--timeout", type=int, default=45)
    parser.add_argument("--dpi", type=int, default=144)
    args = parser.parse_args()
    if args.timeout < 1 or args.dpi < 72:
        parser.error("--timeout debe ser positivo y --dpi al menos 72")
    try:
        renderizar(args.docx.resolve(), args.out.resolve(), args.timeout, args.dpi)
        return 0
    except (FileNotFoundError, RuntimeError, TimeoutError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
