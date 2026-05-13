# RB-001 — User Cannot Access AI Service

## Purpose

Triage a user or project team that cannot access a GenAI / AI Platform service.

## Symptoms

- 401 Unauthorized
- 403 Forbidden
- Endpoint access denied
- User can access other services but not the AI service
- Project team reports blocked work

## Initial checks

1. Confirm affected user and project.
2. Confirm timestamp and timezone.
3. Collect screenshot or exact error message.
4. Confirm endpoint or service URL.
5. Confirm whether the issue affects one user or multiple users.
6. Check whether the user recently changed role, team or group.
7. Check service health or known incidents.
8. Collect request ID or correlation ID if available.

## Likely causes

- Authentication failure
- Missing group membership
- Missing RBAC permission
- Expired or invalid API key
- Wrong endpoint
- Conditional Access-style restriction
- Platform-side issue

## Escalation

Escalate to the identity or platform team when permissions, RBAC, endpoint configuration or deployment ownership cannot be validated by support.

## Evidence to include

- User
- Project/team
- Error code
- Timestamp
- Endpoint
- Request ID
- Business impact
- Troubleshooting already performed
