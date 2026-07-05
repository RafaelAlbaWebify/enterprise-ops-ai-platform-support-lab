# Flagship Migration Map

This repository is a supporting archive and incubator.

The goal is not to keep expanding it forever. The goal is to use it as a staging area for realistic support scenarios, then move mature material into the correct flagship repository.

## Target Flagships

| Material type | Destination flagship | Reason |
|---|---|---|
| Identity/access scenarios | TRACE | TRACE is my IAM and access-diagnostics flagship. |
| Application/API/log incidents | INFIOS | INFIOS will be my Application Support workbench. |
| Defensive security evidence | CustosOps | CustosOps is my SOC and security-hygiene evidence console. |
| Website/domain/workflow checks | WATCH | WATCH will be my automation and operational monitoring workbench. |
| DNS/infrastructure/service/dependency evidence | OPSCORE | OPSCORE will be my Infrastructure / Production Operations workbench. |
| AI platform/source intelligence/report workflows | YTIS | YTIS will be my AI Development and GenAI application flagship. |

## Migration Rule

A scenario should move out of this lab only when it has enough structure to be useful in a flagship:

```text
scenario
  -> sample evidence
  -> analysis notes
  -> safe next steps
  -> what not to change yet
  -> ticket / escalation note
  -> runbook or report output
```

## What Should Stay Here

This repository can keep:

- early notes
- rough experiments
- training exercises
- unfinished lab ideas
- broad interview-practice material
- VM/lab foundation notes

## What Should Move To Flagships

Move material when it becomes:

- a repeatable diagnostic workflow
- a realistic support scenario
- a reusable runbook
- a public-safe sample report
- a tool/module feature
- a strong portfolio walkthrough

## Priority Migration Candidates

1. AI Platform 403 incident -> INFIOS or YTIS
2. Basic pipeline failure triage -> INFIOS
3. Identity/access troubleshooting notes -> TRACE
4. DNS/endpoint scenarios -> OPSCORE or supporting utilities
5. AI Platform Operations concepts -> YTIS

## Boundary

This lab should not become a seventh flagship.

If a new idea does not clearly belong to TRACE, INFIOS, CustosOps, WATCH, OPSCORE or YTIS, I should pause before adding it publicly.
