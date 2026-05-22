# Sample Output

This example shows the type of support evidence this lab is meant to produce.

## Incident Summary

| Field | Example |
| --- | --- |
| Symptom | User receives 403 when calling AI platform endpoint. |
| Scope | One user, one API route, same network as working users. |
| Initial Layer | Authorization, not general connectivity. |
| Evidence | Token valid, endpoint reachable, user lacks required role. |
| Escalation Target | Identity/platform owner. |

## Example Escalation Note

```text
Impact: One user blocked from AI platform request.
Evidence collected: API returns 403, network connectivity works, token is accepted, other users can access same endpoint.
Likely cause: User authorization or role assignment mismatch.
Requested action: Validate group membership, role assignment and recent access changes for affected user.
```

## Support Interpretation

The goal is not to solve every platform issue inside first-line support. The goal is to collect enough evidence to route the incident accurately and reduce back-and-forth with engineering teams.
