# RB-005 — Pipeline Failure Basic Triage

## Purpose

Support-level triage for a failed Azure DevOps or CI/CD pipeline.

## Initial checks

1. Identify pipeline name.
2. Identify branch.
3. Identify commit.
4. Identify stage, job and task that failed.
5. Read the first clear error message.
6. Check recent changes.
7. Confirm affected environment.
8. Confirm whether deployment reached production or failed before deployment.
9. Check whether rollback is required.

## Common failure areas

- Build failed
- Test failed
- Missing variable or secret
- Permission issue
- Agent issue
- Artifact missing
- Deployment target unavailable
- YAML syntax issue

## Escalation

Escalate to DevOps Dev with:

- Pipeline URL
- Failed stage/job/task
- Error message
- Commit and branch
- Time of failure
- Business impact
- Whether rollback is required
