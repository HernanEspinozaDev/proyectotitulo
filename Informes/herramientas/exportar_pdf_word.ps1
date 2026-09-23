param(
    [Parameter(Mandatory = $true)][string]$Source,
    [Parameter(Mandatory = $true)][string]$Pdf,
    [Parameter(Mandatory = $true)][string]$PidFile
)

$ErrorActionPreference = 'Stop'
$word = $null
$documento = $null
$fallo = $false

try {
    $anteriores = @(Get-Process WINWORD -ErrorAction SilentlyContinue | ForEach-Object Id)
    Write-Output 'create-start'
    $word = New-Object -ComObject Word.Application
    $nuevos = @(Get-Process WINWORD -ErrorAction SilentlyContinue | Where-Object { $anteriores -notcontains $_.Id })
    if ($nuevos.Count -ne 1) { throw "No se pudo identificar una instancia nueva de Word: $($nuevos.Count) procesos" }
    [System.IO.File]::WriteAllText($PidFile, [string]$nuevos[0].Id)
    Write-Output "word-pid=$($nuevos[0].Id)"

    $word.Visible = $false
    $word.DisplayAlerts = 0
    $word.ScreenUpdating = $false
    $word.AutomationSecurity = 3
    $word.Options.UpdateLinksAtOpen = $false
    Write-Output 'open-start'
    $documento = $word.Documents.OpenNoRepairDialog($Source, $false, $true)
    Write-Output "open-ok pages=$($documento.ComputeStatistics(2))"
    Write-Output 'export-start'
    $documento.ExportAsFixedFormat($Pdf, 17)
    Write-Output 'export-ok'
} catch {
    $fallo = $true
    Write-Output "ERROR: $($_.Exception.ToString())"
} finally {
    if ($null -ne $documento) {
        try { $guardar = 0; $documento.Close([ref]$guardar) | Out-Null; Write-Output 'document-closed' }
        catch { Write-Output "close-error: $($_.Exception.Message)" }
        [void][System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($documento)
    }
    if ($null -ne $word) {
        try { $guardar = 0; $word.Quit([ref]$guardar) | Out-Null; Write-Output 'word-quit' }
        catch { Write-Output "quit-error: $($_.Exception.Message)" }
        [void][System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($word)
    }
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}

if ($fallo) { exit 1 }
