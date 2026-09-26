# RB-006 — Intune non-compliant device triage

## Objective
Investigate a Windows device reported as non-compliant without assuming that the compliance state identifies the root cause.

## Evidence to collect
- device compliance state;
- last management sync;
- BitLocker/encryption state;
- Secure Boot state;
- assigned compliance/configuration policy context;
- local endpoint evidence where available.

## Workflow
1. Confirm the affected device and user impact.
2. Review the exported Intune evidence.
3. Correlate compliance, encryption, Secure Boot and last-sync state.
4. Compare with local endpoint evidence if available.
5. Record missing evidence explicitly.
6. Escalate with the evidence package when policy ownership or tenant-side action is required.

## Safe boundary
Do not change compliance policy, disable security controls, rotate recovery keys or force remediation from this lab.

## Portfolio exercise
```powershell
python scripts/python/analyze_ops_evidence.py --kind intune --input examples/modern-workplace/intune-device-export.sample.json
```
