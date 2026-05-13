# Architecture Overview

## Lab objective

The lab is organised in operational layers. Each layer supports either AI Platform Operations, IT Support Engineering, or both.

## Layers

1. Documentation and evidence
2. Windows / workstation support
3. Windows Server / Linux administration
4. Identity and access
5. Microsoft 365 / Azure support
6. Virtualization
7. Networking and VLAN fundamentals
8. AI Platform Operations
9. Model lifecycle / MLOps support
10. DevOps / pipeline support
11. Monitoring and incident management
12. AI tools / local AI

## MVP architecture

```text
User / Project Team
      |
      v
Support / Operations
      |
      +--> Identity checks
      +--> Endpoint / API checks
      +--> Logs and error codes
      +--> Monitoring / service health
      +--> Pipeline status
      |
      v
Escalation
      |
      +--> Identity team
      +--> Platform team
      +--> DevOps Dev
      +--> Infrastructure team
      +--> Service Manager
```

## Scope

This is a support-focused lab. It simulates operational scenarios and documents how to troubleshoot, escalate and improve support processes.
