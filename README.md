# Enterprise Ops + AI Platform Support Lab

> Active supporting lab and incubator for support scenarios that feed the main portfolio projects.

This repository is a practical homelab focused on IT Operations, Microsoft 365 and identity support, Modern Workplace evidence, Azure/AWS operational troubleshooting, AI platform support scenarios, incident handling, documentation, monitoring awareness and support-level DevOps troubleshooting.

It is not positioned as a flagship product. It remains active as a **supporting lab and incubator** where practice material, walkthroughs and evidence packs can be developed before the strongest pieces are promoted into TRACE, INFIOS, WATCH, OPSCORE or YTIS.

The previous `homelab-virtualbox-foundation` material has been consolidated here under `lab-foundation/virtualbox/`.

## Portfolio role

| Status | Purpose |
|---|---|
| Active supporting lab / incubator | Source material for TRACE, INFIOS, WATCH, OPSCORE and YTIS |

## Purpose

This repository shows operational support thinking rather than deep platform engineering. The goal is to demonstrate how I approach incidents, collect evidence, document findings and escalate clearly in enterprise-style environments.

## How this lab feeds the flagships

| Material in this lab | Destination flagship |
|---|---|
| Identity and access troubleshooting | TRACE |
| API errors, HTTP status codes, application support walkthroughs | INFIOS |
| Website/service checks, workflow automation ideas | WATCH |
| DNS, endpoint, VM, infrastructure and dependency evidence | OPSCORE |
| AI platform support, source intelligence and report thinking | YTIS |

## Cloud + Modern Workplace evidence lane

The lab now includes a tested, deterministic offline analyzer for public-safe or synthetic **Intune, Azure and AWS operational evidence**.

```powershell
python scripts/python/analyze_ops_evidence.py --kind intune --input examples/modern-workplace/intune-device-export.sample.json
python scripts/python/analyze_ops_evidence.py --kind azure --input examples/cloud/azure-vm-evidence.sample.json
python scripts/python/analyze_ops_evidence.py --kind aws --input examples/cloud/aws-ec2-evidence.sample.json
```

The analyzer produces structured findings with severity, exact evidence and a safe next check. It does not connect to live tenants/cloud accounts and performs no remediation.

See [Cloud + Modern Workplace evidence lane](docs/cloud-modern-workplace-evidence-lane.md) and the new Intune/Azure/AWS runbooks.

## What this lab demonstrates

- Modern Workplace / Intune evidence interpretation
- Azure and AWS operations evidence triage
- Deterministic offline analysis with automated tests
- Incident handling and triage
- SLA-aware troubleshooting
- Identity and access troubleshooting
- API error interpretation
- Basic pipeline failure triage
- Windows support evidence collection
- Documentation and runbook improvement
- Knowledge base writing
- Escalation notes and handover quality
- AI platform operations support concepts
- Practical lab foundations for DNS, endpoint and access scenarios

## Positioning boundary

This lab is not intended to present me as a senior DevOps engineer, Azure AI engineer, MLOps engineer, VMware architect, network engineer or senior Python developer.

It is designed to show that I can support users and projects in enterprise environments, interpret endpoint-management and cloud-operational evidence, collect facts, understand symptoms, document findings and escalate to the right technical teams. Synthetic fixtures and offline exports do not represent production ownership of Intune, Azure or AWS.

## Current status

Completed so far:

- Initial repository structure
- Support-focused README
- Basic PowerShell support scripts
- Basic Python API support scripts
- Local script validation notes
- AI Platform 403 incident walkthrough
- Basic pipeline failure walkthrough
- Service improvement log
- VirtualBox lab foundation consolidated from the old homelab repository
- Tested Intune, Azure and AWS evidence analyzer with synthetic fixtures
- Intune non-compliance, Azure connectivity and AWS availability runbooks
- GitHub Actions verification for the new evidence lane

Planned improvements:

- Expand runbooks with practical outputs
- Add more incident scenarios
- Improve pipeline examples
- Add Windows Server and Linux VM practice notes
- Add virtualization and networking practice gradually
- Turn the VirtualBox foundation scenarios into completed evidence packs
- Promote mature scenarios into the relevant flagship repository

## Key walkthroughs

- [Documentation Index](docs/index.md)
- [AI Platform 403 Forbidden Incident](docs/interview-walkthrough-ai-platform-403.md)
- [Basic Pipeline Failure Triage](docs/interview-walkthrough-pipeline-failure.md)
- [How to Explain This Lab in Interviews](docs/how-to-explain-this-lab-in-interviews.md)
- [VirtualBox Lab Foundation](lab-foundation/virtualbox/README.md)
- [Cloud + Modern Workplace Evidence Lane](docs/cloud-modern-workplace-evidence-lane.md)
- [Intune non-compliant device triage](runbooks/rb-006-intune-noncompliant-device.md)
- [Azure VM connectivity triage](runbooks/rb-007-azure-vm-connectivity.md)
- [AWS EC2 availability triage](runbooks/rb-008-aws-ec2-availability.md)

## Tested support scripts

### PowerShell

- [Get-WindowsSupportSnapshot.ps1](scripts/powershell/Get-WindowsSupportSnapshot.ps1)
- [Check-ServiceStatus.ps1](scripts/powershell/Check-ServiceStatus.ps1)

These scripts support basic Windows checks such as service status, OS information, disk space, network configuration and recent system errors.

### Python

- [api_health_check.py](scripts/python/api_health_check.py)
- [simulate_ai_api_errors.py](scripts/python/simulate_ai_api_errors.py)
- [analyze_ops_evidence.py](scripts/python/analyze_ops_evidence.py) — Intune, Azure and AWS evidence analysis

These scripts support basic API troubleshooting practice, including endpoint checks, latency measurement and HTTP status-code interpretation.

## Repository areas

```text
docs/            Architecture, roadmap and interview explanations
runbooks/        Repeatable operational procedures
kb/              Knowledge base articles
incidents/       Sample incident tickets and support scenarios
scripts/         Small PowerShell and Python support scripts
pipelines/       Basic Azure DevOps pipeline example
lab-notes/       Lessons learned, improvements and escalation examples
examples/        Sample outputs and portfolio-friendly evidence
lab-foundation/  Practical VM/lab foundations for support scenarios
```

## Example output

See [examples/sample-output.md](examples/sample-output.md) for a short example of how support evidence is summarized for escalation.
