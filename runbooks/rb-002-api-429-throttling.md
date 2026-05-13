# RB-002 — API 429 Throttling

## Purpose

Handle AI Platform requests failing with 429 Too Many Requests.

## Meaning

429 usually indicates rate limiting, quota exhaustion or throttling.

## Initial checks

1. Confirm affected user, application or project.
2. Confirm error timestamp.
3. Check whether the issue is intermittent or constant.
4. Ask whether traffic volume recently increased.
5. Check whether retries are configured.
6. Check whether other projects are affected.
7. Collect request ID and response headers if available.

## Likely causes

- Rate limit reached
- Quota exhausted
- Too many requests in a short period
- Inefficient retry pattern
- Shared deployment capacity used by another team

## Support action

- Ask the user to retry after a short period if appropriate.
- Check whether the issue is isolated or widespread.
- Document frequency and business impact.
- Escalate to platform owner if quota change, capacity review or deployment change is needed.

## Escalation note

Include error code, request volume pattern, timestamps, affected project, business impact and whether retry reduces the issue.
