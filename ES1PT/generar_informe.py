import os
import subprocess
import glob

def generar_informe_docx():
    print("Iniciando la generación del informe ES1...")
    
    # Directorio actual donde están los archivos MD
    directorio = os.getcwd()
    
    # Buscar todos los archivos que empiecen con "0" y terminen en ".md"
    archivos_md = [f for f in glob.glob(os.path.join(directorio, "0*.md")) if not os.path.basename(f).startswith("00_")]
    
    # Ordenar los archivos alfabéticamente/numéricamente para asegurar el orden (01 al 09)
    archivos_md.sort()
    
    if not archivos_md:
        print("Error: No se encontraron archivos Markdown (01_... a 09_...) en el directorio.")
        return
        
    print(f"Se encontraron {len(archivos_md)} capítulos para concatenar:")
    for archivo in archivos_md:
        print(f" - {os.path.basename(archivo)}")
        
    # Nombre del archivo de salida
    archivo_salida = "Informe_Final_ES1.docx"
    
    # Construir el comando de Pandoc
    # pandoc 01_Intro.md 02_Problema.md ... -o Informe_Final_ES1.docx
    comando = ["pandoc"] + archivos_md + ["-o", archivo_salida]
    
    print("\nEjecutando Pandoc para generar el DOCX...")
    try:
        # Ejecutar el comando
        subprocess.run(comando, check=True)
        print(f"\n[Exito] El informe ha sido generado correctamente en: {archivo_salida}")
        print("Nota: Los bloques de codigo Mermaid (Diagramas) se exportan como texto. Recuerda reemplazarlos por las imagenes PNG en tu Word final.")
    except subprocess.CalledProcessError as e:
        print(f"\n[Error] al ejecutar Pandoc: {e}")
    except FileNotFoundError:
        print("\n[Error] Pandoc no esta instalado o no esta en el PATH del sistema.")
        print("Por favor, instala Pandoc desde https://pandoc.org/installing.html")

if __name__ == "__main__":
    generar_informe_docx()
