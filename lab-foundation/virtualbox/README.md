# VirtualBox Lab Foundation

This folder keeps the practical VirtualBox foundation that was originally tracked in the separate `homelab-virtualbox-foundation` repository.

It belongs here because the VirtualBox lab is not a separate product. It is the infrastructure practice layer that supports the wider Enterprise Ops + AI Platform Support Lab.

## Purpose

Build a small, repeatable lab environment where common IT support and application support situations can be practised safely.

The focus is not virtualization architecture. The focus is support evidence:

- what failed
- what was checked
- what changed
- what fixed the issue
- what should be documented for next time

## Planned Lab Shape

```text
Host machine
└── VirtualBox
    ├── Windows Server VM
    │   ├── DNS practice
    │   ├── user and group practice
    │   └── shared resource practice
    ├── Windows Client VM
    │   ├── endpoint checks
    │   ├── user login scenarios
    │   └── troubleshooting exercises
    └── Optional Linux VM
        ├── connectivity checks
        └── basic service validation
```

## First Practice Areas

- DNS record mismatch causing application access confusion
- User group membership issue affecting shared resource access
- Windows client baseline check after configuration drift
- Service unavailable scenario with evidence collection
- Support ticket to knowledge base article workflow

## How This Connects To The Main Lab

This foundation supports the wider lab by providing realistic infrastructure and endpoint scenarios for:

- identity and access troubleshooting
- DNS and name-resolution checks
- endpoint support evidence
- basic server/client relationships
- incident notes and escalation notes
- runbook creation
- support interview explanations

## What This Is Not

This folder is not intended to present deep virtualization, cloud architecture or senior infrastructure engineering expertise.

It is a support-oriented practice foundation for building evidence-based troubleshooting habits.