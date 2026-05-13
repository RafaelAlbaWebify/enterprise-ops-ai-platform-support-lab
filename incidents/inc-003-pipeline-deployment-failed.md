# INC-003 — Pipeline Deployment Failed

## Summary

A deployment pipeline failed during a release.

## Impact

New AI Platform feature was not deployed to test environment.

## Symptoms

- Pipeline failed.
- Build completed.
- Deployment stage failed.
- No production impact.

## Initial checks

- Identified pipeline.
- Identified branch and commit.
- Located failed stage, job and task.
- Captured first clear error message.
- Checked whether artifact was created.
- Confirmed target environment.

## Suspected cause

Missing variable, secret or deployment permission.

## Escalation

Escalate to DevOps Dev with pipeline evidence and operational impact.
