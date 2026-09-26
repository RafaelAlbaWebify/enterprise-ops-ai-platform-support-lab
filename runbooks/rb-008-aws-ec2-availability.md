# RB-008 — AWS EC2 availability triage

## Objective
Separate EC2 instance state, AWS status checks, network reachability and workload evidence during an availability incident.

## Evidence to collect
- EC2 instance state;
- system/instance status-check result;
- network reachability;
- security-group/NACL/route context;
- CPU and disk pressure;
- CloudWatch timeline and recent changes.

## Workflow
1. Confirm impact and affected service.
2. Review instance state and status-check evidence separately.
3. Validate network controls and DNS before treating reachability as an instance failure.
4. Correlate resource pressure with workload evidence.
5. Produce an escalation note with supporting and missing evidence.

## Safe boundary
The lab does not reboot, stop, resize, modify security groups or alter AWS resources.

## Portfolio exercise
```powershell
python scripts/python/analyze_ops_evidence.py --kind aws --input examples/cloud/aws-ec2-evidence.sample.json
```
