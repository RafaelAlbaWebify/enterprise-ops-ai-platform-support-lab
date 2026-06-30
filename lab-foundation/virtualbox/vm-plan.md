# VirtualBox VM Plan

This is a simple starting plan for a support-oriented VirtualBox lab.

The goal is to create enough realism for troubleshooting practice without turning the lab into a complex infrastructure project.

## Minimum Lab

```text
LAB-DC01
Purpose: Windows Server practice VM
Roles: DNS, users, groups, shared resource practice

LAB-WIN11-01
Purpose: Windows client practice VM
Roles: login tests, endpoint checks, access tests, support evidence collection
```

## Optional VM

```text
LAB-LINUX-01
Purpose: basic Linux or service validation practice
Roles: ping, DNS lookup, simple service checks, log reading practice
```

## Naming Convention

Use simple names that make the lab readable:

```text
LAB-DC01       Windows Server / DNS / identity practice
LAB-WIN11-01   Windows client practice
LAB-LINUX-01   Optional Linux or service VM
```

## Network Intent

Start with one simple lab network. Do not overcomplicate segmentation until basic troubleshooting scenarios are working.

Initial checks:

- each VM has a clear hostname
- each VM has predictable IP configuration
- the Windows client can resolve expected names
- the Windows client can reach expected lab resources
- failed scenarios are created deliberately and documented

## Evidence Rule

Every configuration change should produce a short note:

```text
What changed:
Why it changed:
How it was validated:
Rollback or risk:
Documentation updated:
```

## When To Expand

Only expand the lab after the first support scenarios are documented.

Possible later additions:

- separate app/server VM
- simple web application endpoint
- log forwarding practice
- basic monitoring checks
- integration with PowerShell evidence scripts

Do not add complexity just to make the lab look bigger. Add complexity only when it creates better support practice.