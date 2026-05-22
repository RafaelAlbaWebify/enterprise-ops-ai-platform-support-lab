# Enterprise Ops + AI Platform Support Lab

A practical homelab focused on IT Operations, Microsoft 365 and identity support, AI platform support scenarios, incident handling, documentation, monitoring awareness and support-level DevOps troubleshooting.

## Purpose

This repository shows operational support thinking rather than deep platform engineering. The goal is to demonstrate how I approach incidents, collect evidence, document findings and escalate clearly in enterprise-style environments.

## What This Lab Demonstrates

- Incident handling and triage
- SLA-aware troubleshooting
- Identity and access troubleshooting
- API error interpretation
- Basic pipeline failure triage
- Windows support evidence collection
- Documentation and runbook improvement
- Knowledge base writing
- Escalation notes and handover quality
- AI Platform Operations support concepts

## Important Positioning

This lab is not intended to present me as a senior DevOps engineer, Azure AI engineer, MLOps engineer, VMware architect, network engineer or senior Python developer.

It is designed to show that I can support users and projects in enterprise environments, collect evidence, understand symptoms, document findings and escalate to the right technical teams.

## Current Status

Completed so far:

- Initial repository structure
- Support-focused README
- Basic PowerShell support scripts
- Basic Python API support scripts
- Local script validation notes
- AI Platform 403 incident walkthrough
- Basic pipeline failure walkthrough
- Service improvement log

Next planned improvements:

- Add more tested examples
- Expand runbooks with practical outputs
- Add more incident scenarios
- Improve pipeline examples
- Add Windows Server and Linux VM practice notes
- Add virtualization and networking practice gradually

## Key Walkthroughs

- [Documentation Index](docs/index.md)
- [AI Platform 403 Forbidden Incident](docs/interview-walkthrough-ai-platform-403.md)
- [Basic Pipeline Failure Triage](docs/interview-walkthrough-pipeline-failure.md)
- [How to Explain This Lab in Interviews](docs/how-to-explain-this-lab-in-interviews.md)

## Tested Support Scripts

### PowerShell

- [Get-WindowsSupportSnapshot.ps1](scripts/powershell/Get-WindowsSupportSnapshot.ps1)
- [Check-ServiceStatus.ps1](scripts/powershell/Check-ServiceStatus.ps1)

These scripts are used for basic Windows support checks such as service status, OS information, disk space, network configuration and recent system errors.

### Python

- [api_health_check.py](scripts/python/api_health_check.py)
- [simulate_ai_api_errors.py](scripts/python/simulate_ai_api_errors.py)

These scripts are used for basic API support practice, including endpoint checks, latency measurement and HTTP status code interpretation.

## Documentation Areas

```text
docs/          Architecture, roadmap and interview explanations
runbooks/      Repeatable operational procedures
kb/            Knowledge base articles
incidents/     Sample incident tickets and support scenarios
scripts/       Small PowerShell and Python support scripts
pipelines/     Basic Azure DevOps pipeline example
lab-notes/     Lessons learned, improvements and escalation examples
examples/      Sample outputs and portfolio-friendly evidence
```

## Example Output

See [examples/sample-output.md](examples/sample-output.md) for a short example of how support evidence is summarized for escalation.

## Operational Support Themes

This lab practises how to:

- understand user impact
- separate symptoms from likely root cause
- collect evidence before escalation
- distinguish authentication from authorization issues
- interpret common API errors such as 401, 403, 429 and 500
- review basic pipeline failure information
- document findings in runbooks, KB articles and incident notes
- improve support documentation after testing or repeated issues

## Interview Summary

I built this homelab to connect my IT Operations background with AI Platform Operations and modern infrastructure support. The focus is support readiness: identity and access troubleshooting, API error interpretation, pipeline log awareness, monitoring, escalation, documentation and continual service improvement.

## License

MIT
