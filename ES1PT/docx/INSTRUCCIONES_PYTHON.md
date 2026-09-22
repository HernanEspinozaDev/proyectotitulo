# Instrucciones para usar los scripts de Python

## 1) Preparar el entorno

En la raíz del proyecto, crea un entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r ..\requirements.txt
```

> El archivo `requirements.txt` de la raíz no instala librerías de terceros porque los scripts usan solamente la librería estándar de Python.

## 2) Requisitos del sistema

Antes de ejecutar los scripts, asegúrate de tener instalado:

- Python 3.10 o superior
- Pandoc 3.x y disponible en `PATH`
- Java (JDK/JRE)
- `plantuml.jar` para renderizar diagramas UML

## 3) Scripts disponibles

Los scripts fuente que sí deben quedar en GitHub son:

- `ES1PT/docx/bibliografia.py`
- `ES1PT/docx/generar_informe.py`
- `ES1PT/docx/calibrar_tipos.py`
- `ES1PT/docx/calibrar_word.py`

## 4) Ejemplos de uso

### Extraer y analizar una bibliografía de Word

```powershell
cd ES1PT\docx
python calibrar_word.py "C:\ruta\al\documento.docx"
python calibrar_tipos.py "C:\ruta\al\documento.docx"
```

### Generar el informe

```powershell
cd ES1PT\docx
python generar_informe.py diagramas
python generar_informe.py preprocesar
python generar_informe.py pandoc
python generar_informe.py armar
python generar_informe.py validar
python generar_informe.py todo
```

## 5) Qué no se sube a GitHub

Se excluyen del repositorio estos artefactos generados:

- `ES1PT/docx/build/`
- `ES1PT/docx/calibracion/`
- `__pycache__/`
- entornos virtuales: `.venv`, `venv`, `env`

Esto mantiene el repositorio limpio y evita archivos pesados o reproducibles.
