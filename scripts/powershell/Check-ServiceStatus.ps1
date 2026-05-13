<#
.SYNOPSIS
Checks the status of one or more Windows services.

.EXAMPLE
.\Check-ServiceStatus.ps1 -ServiceNames Spooler,WinRM
#>

param(
    [Parameter(Mandatory=$true)]
    [string[]]$ServiceNames
)

foreach ($ServiceName in $ServiceNames) {
    Write-Host "`nChecking service: $ServiceName"
    $service = Get-Service -Name $ServiceName -ErrorAction SilentlyContinue

    if (-not $service) {
        Write-Host "Result: Service not found"
        continue
    }

    $service | Select-Object Name, DisplayName, Status, StartType | Format-List

    if ($service.Status -ne "Running") {
        Write-Host "Support note: Service is not running. Check Event Viewer before restarting if this is production or business-critical."
    } else {
        Write-Host "Support note: Service is running."
    }
}
