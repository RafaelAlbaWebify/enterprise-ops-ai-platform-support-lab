# RB-007 — Azure VM connectivity triage

## Objective
Structure evidence for a VM/service connectivity incident before any recovery action.

## Evidence to collect
- VM power state;
- Azure Resource Health;
- observed network reachability;
- effective NSG and route context;
- DNS resolution;
- CPU and disk pressure;
- recent changes and monitoring timeline.

## Workflow
1. Confirm business impact and affected endpoint/service.
2. Separate platform-health evidence from guest/workload evidence.
3. Review networking context before assuming the VM is down.
4. Correlate CPU/disk pressure with the incident timeline.
5. Record the safest next check and escalation owner.

## Safe boundary
The lab does not modify NSGs, routes, VMs, disks or Azure resources.

## Portfolio exercise
```powershell
python scripts/python/analyze_ops_evidence.py --kind azure --input examples/cloud/azure-vm-evidence.sample.json
```
