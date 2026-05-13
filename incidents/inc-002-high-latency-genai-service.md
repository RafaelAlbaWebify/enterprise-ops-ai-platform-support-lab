# INC-002 — High Latency in GenAI Service

## Summary

Users report slow responses from GenAI service.

## Impact

Project testing is delayed. No complete outage reported.

## Symptoms

- Requests eventually complete.
- Response time is higher than usual.
- No clear authentication error.
- Some prompts are slower than others.

## Initial checks

- Collected timestamps.
- Confirmed affected users.
- Asked for model/deployment name.
- Asked for approximate prompt size.
- Checked whether issue affects all users or one project.
- Requested request IDs.

## Possible causes

- Increased token usage
- Service capacity issue
- Network latency
- Model deployment performance
- Recent platform change

## Escalation

Escalate to platform team if latency is repeated, affects multiple users or breaches SLA.
