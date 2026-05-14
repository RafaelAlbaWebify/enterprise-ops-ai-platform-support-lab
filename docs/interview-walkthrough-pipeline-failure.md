# Interview Walkthrough — Basic Pipeline Failure Triage

## Scenario

A deployment pipeline fails while releasing a new AI Platform or application change to a test environment.

The pipeline shows a failed stage, job or task.

The business impact is that a new feature, fix or configuration change cannot be deployed as expected.

---

## Initial support mindset

I would not immediately try to fix the code or redesign the pipeline.

As Operations / Application Support, my first responsibility is to understand:

1. What failed?
2. Where did it fail?
3. Who is affected?
4. Is production impacted?
5. Is rollback required?
6. Which team owns the next action?

The goal is to collect clear evidence and escalate to DevOps Dev or the platform team if the fix is outside my support scope.

---

## Information to collect

Before escalating, I would collect:

- pipeline name
- branch
- commit
- pull request if relevant
- failed stage
- failed job
- failed task
- exact error message
- timestamp and timezone
- target environment
- whether the build succeeded
- whether the deployment started
- whether production is affected
- recent changes
- business impact
- rollback requirement

---

## First checks

### 1. Identify where the failure happened

A pipeline can fail in different places:

- repository checkout
- build
- test
- package/artifact creation
- deployment
- environment approval
- variable or secret access
- connection to target service
- post-deployment validation

Support value:

Knowing where the failure happened helps identify the owner and next step.

---

### 2. Check whether this is build or deployment related

If the build failed, the issue may be related to:

- code
- dependencies
- tests
- build agent
- package restore
- YAML syntax

If the deployment failed, the issue may be related to:

- environment permissions
- missing variables
- missing secrets
- target service unavailable
- wrong configuration
- deployment approval
- infrastructure issue

---

### 3. Check the first clear error

I would look for the first meaningful error in the pipeline logs.

I would avoid only copying the final generic message, because many pipelines end with messages like:

```text
Job failed
Task failed
Process completed with exit code 1
```

Those messages confirm failure, but they may not explain the root cause.

---

### 4. Check recent changes

Possible recent changes:

- new commit
- merged pull request
- YAML pipeline change
- new variable or secret requirement
- permission change
- environment change
- service connection change
- new deployment target
- new AI Platform configuration

---

## Possible root causes

| Area | Possible cause |
|---|---|
| Code | Recent commit introduced an error |
| Build | Dependency or package restore failed |
| Test | Automated test failed |
| YAML | Pipeline syntax or indentation issue |
| Variables | Required variable is missing |
| Secrets | Secret is missing, expired or inaccessible |
| Permissions | Pipeline cannot access target environment |
| Agent | Build agent unavailable or misconfigured |
| Artifact | Expected artifact was not created |
| Environment | Deployment target unavailable |
| Platform | Target AI Platform service or API is unavailable |

---

## Escalation note example

Pipeline X failed during deployment to the test environment.

Collected evidence:

- pipeline:
- branch:
- commit:
- failed stage:
- failed job:
- failed task:
- timestamp:
- target environment:
- first clear error:
- recent change:
- production impact:
- rollback required:

Initial assessment: the build completed successfully, but the deployment stage failed. The error suggests a missing variable, secret or permission issue when deploying to the target environment.

Please review the deployment configuration, service connection and environment permissions.

---

## User-facing update

The deployment pipeline failed before the change could be released to the target environment.

We are reviewing the failed pipeline stage and have collected the relevant logs, timestamp and deployment context.

At the moment, production impact has not been confirmed. We have escalated the failure to the DevOps / platform team for review.

---

## Operational questions I would ask

- Is this blocking a business-critical release?
- Is this affecting production or only test/dev?
- Has this pipeline worked before?
- Did the failure start after a recent commit or configuration change?
- Is the failure repeatable?
- Is rollback required?
- Is there an SLA or release deadline at risk?
- Who owns the failed component?

---

## Rollback consideration

If the failure happened before deployment, rollback may not be required.

If the failure happened during or after deployment, I would check:

- whether the environment is partially updated
- whether users are affected
- whether previous version is still available
- whether rollback is manual or automated
- who is authorised to approve rollback

As support, I would not trigger rollback without ownership or approval.

---

## KB improvement after resolution

After resolution, I would update the KB with:

- confirmed root cause
- failed stage/job/task
- error pattern
- owner team
- resolution steps
- prevention notes
- what evidence to collect next time

---

## Interview explanation

In an interview, I would explain this as follows:

If a pipeline fails, I would first identify where it failed: build, test, artifact creation, deployment or validation. Then I would collect the branch, commit, failed stage, failed job, failed task, first clear error message, timestamp and affected environment.

I would check whether production is impacted and whether rollback is required. If the issue is related to code, YAML, secrets, service connections or environment permissions outside my scope, I would escalate to DevOps Dev or the platform team with clear evidence.

My role is not to redesign the CI/CD process, but to support the incident, collect useful logs, communicate impact and help the technical team resolve it faster.

---

## What I would not claim

I would not claim that I design complex production pipelines or own release engineering.

My role would be to understand pipeline concepts at support level, read basic logs, identify the failed stage or task, collect evidence, communicate impact and escalate clearly.
