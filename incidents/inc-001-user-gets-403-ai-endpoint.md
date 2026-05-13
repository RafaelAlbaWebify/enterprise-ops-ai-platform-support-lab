# INC-001 — User Gets 403 Accessing AI Endpoint

## Summary

A user receives 403 Forbidden when accessing a GenAI endpoint.

## Impact

One project user is blocked from testing the AI service.

## Symptoms

- User can sign in.
- User can access the portal.
- User cannot call the AI endpoint.
- Error: 403 Forbidden.

## Initial analysis

Authentication appears successful. The issue is likely authorization-related.

## Checks performed

- Confirmed user identity.
- Confirmed endpoint name.
- Compared affected user with working user.
- Requested screenshot and timestamp.
- Asked for request ID.

## Suspected cause

Missing group membership or RBAC permission.

## Escalation

Escalate to platform/identity team to validate endpoint permissions and group assignment.

## KB improvement

Add 403 scenario to AI Platform API error code KB.
