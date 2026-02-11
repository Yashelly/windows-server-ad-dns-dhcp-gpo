<#
Domain triage snapshot used during lab validation (non-destructive).
Writes timestamped raw outputs to ./reports/<timestamp>/ (kept local during the build).
# Note: Sanitized excerpts may be published under ./99-evidence/exports/ and referenced by EVD-* IDs.
#>
$ts = Get-Date -Format "yyyyMMdd-HHmmss"
$dir = ".\reports\$ts"
New-Item -ItemType Directory -Force -Path $dir | Out-Null

ipconfig /all | Out-File -Encoding utf8 "$dir\ipconfig-all.txt"
whoami /all | Out-File -Encoding utf8 "$dir\whoami-all.txt"
gpresult /h "$dir\gpresult.html" | Out-Null

try {
  Get-WinEvent -LogName "Microsoft-Windows-GroupPolicy/Operational" -MaxEvents 80 |
    Select-Object TimeCreated, Id, LevelDisplayName, Message |
    Out-File -Encoding utf8 "$dir\gpo-events.txt"
} catch {}

Write-Host "Saved triage to $dir"
