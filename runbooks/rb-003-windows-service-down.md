# RB-003 — Windows Service Down

## Purpose

Triage a Windows service that is stopped or failing.

## Initial checks

1. Identify the service name.
2. Check current status.
3. Check startup type.
4. Review recent Event Viewer logs.
5. Confirm user or business impact.
6. Check whether the server or workstation was recently patched or rebooted.
7. Restart the service only if it is safe and within support scope.

## Useful PowerShell

```powershell
Get-Service -Name "Spooler"
Get-EventLog -LogName System -Newest 20
```

## Escalation

Escalate if:

- The service stops repeatedly.
- The service is business-critical.
- There are permission, dependency or application errors.
- Restarting the service could cause production impact.

## Documentation

Record service name, timestamp, event log errors, action taken and result.
