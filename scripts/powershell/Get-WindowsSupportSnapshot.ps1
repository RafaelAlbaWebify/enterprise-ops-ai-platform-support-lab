<#
.SYNOPSIS
Collects basic Windows support information for troubleshooting.

.DESCRIPTION
This is a support-level script intended to gather common information before escalation.
It does not make system changes.
#>

$Snapshot = [ordered]@{
    ComputerName = $env:COMPUTERNAME
    UserName = $env:USERNAME
    DateTime = Get-Date
    OS = (Get-CimInstance Win32_OperatingSystem).Caption
    OSVersion = (Get-CimInstance Win32_OperatingSystem).Version
    LastBootTime = (Get-CimInstance Win32_OperatingSystem).LastBootUpTime
}

Write-Host "=== Windows Support Snapshot ==="
$Snapshot.GetEnumerator() | ForEach-Object {
    Write-Host "$($_.Key): $($_.Value)"
}

Write-Host "`n=== Disk Free Space ==="
Get-CimInstance Win32_LogicalDisk -Filter "DriveType=3" |
    Select-Object DeviceID,
                  @{Name="FreeGB";Expression={[math]::Round($_.FreeSpace / 1GB, 2)}},
                  @{Name="SizeGB";Expression={[math]::Round($_.Size / 1GB, 2)}} |
    Format-Table -AutoSize

Write-Host "`n=== Network Configuration ==="

Get-NetIPConfiguration | ForEach-Object {
    $interfaceName = $_.InterfaceAlias

    $ipv4 = if ($_.IPv4Address) {
        ($_.IPv4Address | ForEach-Object { $_.IPAddress }) -join ", "
    } else {
        "No IPv4 address"
    }

    $gateway = if ($_.IPv4DefaultGateway) {
        ($_.IPv4DefaultGateway | ForEach-Object { $_.NextHop }) -join ", "
    } else {
        "No default gateway"
    }

    $dnsServers = if ($_.DNSServer -and $_.DNSServer.ServerAddresses) {
        ($_.DNSServer.ServerAddresses) -join ", "
    } else {
        "No DNS servers"
    }

    Write-Host "Interface: $interfaceName"
    Write-Host "IPv4: $ipv4"
    Write-Host "Gateway: $gateway"
    Write-Host "DNS: $dnsServers"
    Write-Host ""
}

Write-Host "`n=== Recently Stopped Automatic Services ==="
Get-Service |
    Where-Object { $_.StartType -eq "Automatic" -and $_.Status -ne "Running" } |
    Select-Object Name, DisplayName, Status, StartType |
    Format-Table -AutoSize

Write-Host "`n=== Recent System Errors ==="
Get-WinEvent -LogName System -MaxEvents 30 |
    Where-Object { $_.LevelDisplayName -in @("Error", "Critical") } |
    Select-Object TimeCreated, ProviderName, Id, LevelDisplayName, Message |
    Format-List
