# actualizar_campos.ps1
#
# Actualiza los campos de los documentos generados con Word y los guarda:
#   - el índice de contenido (con capítulos y números de página)
#   - el índice de tablas y el de figuras
#   - las citas (CITATION) y la lista de referencias (BIBLIOGRAPHY)
#
# Equivale a abrir cada documento y pulsar Ctrl+A -> F9, sin intervención manual.
# Ejecutar DESPUÉS de regenerar con generar_informe.py:
#
#   powershell -NoProfile -ExecutionPolicy Bypass -File .\actualizar_campos.ps1
#
# Se puede indicar otro documento:
#   powershell -File .\actualizar_campos.ps1 -Ruta "build\Anexo_A_...docx"
#
# Recorre TODAS las historias del documento (StoryRanges) porque el índice vive
# en un cuadro de texto y Fields.Update() por sí solo no lo alcanza.
# Usa una instancia de Word por documento (un documento grande con muchos campos
# puede voltear la instancia) y continúa con el resto si uno falla.

param(
    [string[]]$Ruta
)

$ErrorActionPreference = 'Continue'
$carpeta = Join-Path $PSScriptRoot "build"

if (-not $Ruta) {
    $Ruta = @(Join-Path $carpeta "Informe_Final.docx")
    Get-ChildItem (Join-Path $carpeta "Anexo_*.docx") | Sort-Object Name | ForEach-Object {
        $Ruta += $_.FullName
    }
}

$procesados = 0
$fallidos = @()
$omitidos = @()

foreach ($archivo in $Ruta) {
    $nombre = [System.IO.Path]::GetFileName($archivo)
    if (-not (Test-Path $archivo)) {
        Write-Host "ERROR: no existe $nombre" -ForegroundColor Red
        $fallidos += $nombre
        continue
    }
    # ¿abierto en Word?
    try {
        $fs = [System.IO.File]::Open($archivo, 'Open', 'ReadWrite', 'None')
        $fs.Close()
    } catch {
        Write-Host "OMITIDO (abierto en Word): $nombre" -ForegroundColor Yellow
        $omitidos += $nombre
        continue
    }

    $word = $null
    try {
        $word = New-Object -ComObject Word.Application
        $word.Visible = $false
        $word.DisplayAlerts = 0
        $word.AutomationSecurity = 3

        $doc = $word.Documents.Open($archivo, $false, $false)
        try {
            # dos pasadas: el índice necesita la segunda para fijar las páginas
            foreach ($pasada in 1..2) {
                foreach ($toc in $doc.TablesOfContents) { $toc.Update() | Out-Null }
                foreach ($historia in $doc.StoryRanges) {
                    $s = $historia
                    while ($s -ne $null) {
                        $s.Fields.Update() | Out-Null
                        $s = $s.NextStoryRange
                    }
                }
                $doc.Fields.Update() | Out-Null
            }

            $entradas = 0
            foreach ($toc in $doc.TablesOfContents) {
                $entradas += @($toc.Range.Text -split "`r" | Where-Object { $_.Trim().Length -gt 2 }).Count
            }
            $malas = 0
            foreach ($f in $doc.Fields) {
                $r = ""
                try { $r = $f.Result.Text } catch { $r = "" }
                if ($r.Contains('Fuente especificada') -or $r.Contains('Error!')) { $malas++ }
            }

            "=== $nombre"
            "    indices: " + $doc.TablesOfContents.Count + " | entradas: " + $entradas +
                " | errores de campo: " + $malas
            if ($malas -gt 0) { Write-Host "    ADVERTENCIA: campos con error" -ForegroundColor Yellow }

            $doc.Save()
            $procesados++
        }
        finally {
            try { $doc.Close(0) } catch { }
        }
    }
    catch {
        Write-Host "FALLO: $nombre -> " + $_.Exception.Message -ForegroundColor Red
        $fallidos += $nombre
    }
    finally {
        if ($word -ne $null) {
            try { $word.Quit() } catch { }
            try { [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null } catch { }
        }
    }
}

if ($omitidos.Count -gt 0) {
    Write-Host ("Cierra estos documentos y vuelve a ejecutar: " + ($omitidos -join ", ")) -ForegroundColor Yellow
}
if ($fallidos.Count -gt 0) {
    Write-Host ("Con fallo (revisar o reintentar): " + ($fallidos -join ", ")) -ForegroundColor Red
}
Write-Host "OK: $procesados documento(s) actualizados y guardados." -ForegroundColor Green
