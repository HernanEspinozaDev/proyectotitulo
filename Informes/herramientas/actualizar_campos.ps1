# actualizar_campos.ps1
#
# Actualiza los campos de los documentos generados con Word y los guarda:
#   - el índice de contenido (con capítulos y números de página)
#   - el índice de tablas y el de figuras
#   - las citas (CITATION) y la lista de referencias (BIBLIOGRAPHY)
#
# Equivale a abrir cada documento y pulsar Ctrl+A -> F9, sin intervención manual.
# Ejecutar DESPUÉS de generar y validar con el motor compartido:
#
#   python Informes/generar.py actualizar-word ES2PT
#
# Recorre TODAS las historias del documento (StoryRanges) porque el índice vive
# en un cuadro de texto y Fields.Update() por sí solo no lo alcanza.
# Usa una instancia de Word por documento (un documento grande con muchos campos
# puede voltear la instancia) y continúa con el resto si uno falla.

param(
    [Parameter(Mandatory=$true)][string]$Carpeta,
    [string]$EstiloApa,
    [switch]$SoloIndices
)

$ErrorActionPreference = 'Stop'
$carpeta = (Resolve-Path -LiteralPath $Carpeta).Path
$manifest = Get-Content -LiteralPath (Join-Path $carpeta 'generacion.json') -Raw -Encoding UTF8 | ConvertFrom-Json
if (-not $manifest.completa) { throw 'La generación no está completa.' }
$nombres = @($manifest.documentos.PSObject.Properties.Name)
foreach ($nombre in $nombres) {
    if ([System.IO.Path]::GetFileName($nombre) -ne $nombre -or [System.IO.Path]::GetExtension($nombre) -ne '.docx') {
        throw 'El manifiesto contiene una ruta de documento no válida.'
    }
}
$Ruta = @($manifest.documentos.PSObject.Properties.Name | ForEach-Object { Join-Path $carpeta $_ })

# Revisar el estilo instalado ANTES de abrir o guardar si se actualizarán citas.
if (-not $SoloIndices) {
    $candidatos = @()
    if ($EstiloApa) { $candidatos += $EstiloApa }
    $candidatos += (Join-Path $env:APPDATA 'Microsoft/Bibliography/Style/APASeventhEdition.xsl')
    foreach ($baseOffice in @($env:ProgramFiles, ${env:ProgramFiles(x86)})) {
        if ($baseOffice) {
            $candidatos += (Join-Path $baseOffice 'Microsoft Office/root/Office16/Bibliography/Style/APASeventhEdition.xsl')
        }
    }
    $encontrado = @($candidatos | Where-Object { Test-Path -LiteralPath $_ -PathType Leaf })
    if ($encontrado.Count -eq 0) { throw 'No se encontró APASeventhEdition.xsl instalado en Word. No se actualizaron campos.' }
    $xmlEstilo = New-Object System.Xml.XmlDocument
    $xmlEstilo.Load($encontrado[0])
    if ($xmlEstilo.DocumentElement.NamespaceURI -ne 'http://www.w3.org/1999/XSL/Transform') { throw 'El estilo APA no es un XSL válido.' }
}

if (-not $Ruta) { throw 'El manifiesto no contiene documentos.' }

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
            if (-not $SoloIndices) {
                try { $word.Bibliography.BibliographyStyle = $encontrado[0] }
                catch { throw "Word rechazó activar APA 7 mediante BibliographyStyle ($($_.Exception.Message)). No se actualizan las citas ni se guarda el documento." }
                if ($word.Bibliography.BibliographyStyle -notmatch 'APASeventhEdition') {
                    throw 'Word no activó APA 7. No se guarda el documento.'
                }
            }
            # dos pasadas: el índice necesita la segunda para fijar las páginas
            foreach ($pasada in 1..2) {
                foreach ($toc in $doc.TablesOfContents) { $toc.Update() | Out-Null }
                if (-not $SoloIndices) {
                    foreach ($historia in $doc.StoryRanges) {
                        $s = $historia
                        while ($s -ne $null) {
                            $s.Fields.Update() | Out-Null
                            $s = $s.NextStoryRange
                        }
                    }
                    $doc.Fields.Update() | Out-Null
                }
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
            if ($malas -gt 0) { throw 'Se detectaron campos con error; no se guarda el documento.' }

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
if ($fallidos.Count -gt 0 -or $omitidos.Count -gt 0) { exit 1 }
