# Enterprise Ops + AI Platform Support Homelab

A practical homelab focused on IT Operations, Microsoft 365 / identity support, virtualization fundamentals, AI Platform Operations, incident handling, documentation, monitoring and support-level DevOps troubleshooting.

## Purpose

This repository is designed to show operational support thinking:

- Incident handling
- SLA-aware troubleshooting
- Escalation
- Documentation and runbooks
- Knowledge base improvement
- Basic automation
- Monitoring awareness
- AI Platform Operations support concepts
- Azure DevOps support-level understanding
- Windows / Microsoft 365 / identity troubleshooting

## Important positioning

This lab is not intended to present me as:

- A senior DevOps engineer
- A senior Azure AI engineer
- An MLOps engineer
- A VMware architect
- A network engineer
- A senior Python developer

The goal is to demonstrate that I can support users and projects in enterprise environments, collect evidence, troubleshoot methodically, document findings and escalate to the right technical teams.

## Current focus

The first version of this lab focuses on:

- AI Platform Operations support scenarios
- API error interpretation
- Identity and access troubleshooting
- Basic pipeline failure triage
- Windows support evidence collection
- Support documentation and escalation notes

## Key walkthroughs

These files explain realistic support scenarios and how I would handle them in an interview or operational support context:

- [AI Platform 403 Forbidden Incident](docs/interview-walkthrough-ai-platform-403.md)
- [Basic Pipeline Failure Triage](docs/interview-walkthrough-pipeline-failure.md)
- [How to Explain This Lab in Interviews](docs/how-to-explain-this-lab-in-interviews.md)

## Tested support scripts

### PowerShell

- [Get-WindowsSupportSnapshot.ps1](scripts/powershell/Get-WindowsSupportSnapshot.ps1)
- [Check-ServiceStatus.ps1](scripts/powershell/Check-ServiceStatus.ps1)

These scripts are used for basic Windows support checks such as service status, OS information, disk space, network configuration and recent system errors.

### Python

- [api_health_check.py](scripts/python/api_health_check.py)
- [simulate_ai_api_errors.py](scripts/python/simulate_ai_api_errors.py)

These scripts are used for basic API support practice, including endpoint checks, latency measurement and HTTP status code interpretation.

## Documentation areas

```text
docs/          Architecture, roadmap and interview explanations
runbooks/      Repeatable operational procedures
kb/            Knowledge base articles
incidents/     Sample incident tickets and support scenarios
scripts/       Small PowerShell and Python support scripts
pipelines/     Basic Azure DevOps pipeline example
lab-notes/     Lessons learned, improvements and escalation examples
```

## Operational support themes

This lab practises how to:

- understand user impact
- separate symptoms from likely root cause
- collect evidence before escalation
- distinguish authentication from authorization issues
- interpret common API errors such as 401, 403, 429 and 500
- review basic pipeline failure information
- document findings in runbooks, KB articles and incident notes
- improve support documentation after testing or repeated issues

## Interview summary

I built this homelab to connect my real IT Operations background with AI Platform Operations and modern infrastructure support.

The focus is support readiness: identity and access troubleshooting, API error interpretation, pipeline log awareness, monitoring, escalation, documentation and continual service improvement.

This lab is intentionally small and support-focused. It is not designed to simulate a full enterprise AI platform or production DevOps environment.
