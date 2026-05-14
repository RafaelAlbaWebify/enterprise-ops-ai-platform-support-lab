# Interview Walkthrough — AI Platform 403 Forbidden Incident

## Scenario

A user from an internal project team reports that they cannot access a GenAI endpoint.

The user receives:

```text
HTTP 403 Forbidden
```

Other users may or may not be affected. The business impact is that the project team cannot continue testing or using the GenAI service.

---

## Initial support mindset

I would not immediately assume that the AI service is down.

A 403 usually means the user or application is authenticated, but not authorised to access the resource.

So I would separate the problem into two questions:

1. Can the user authenticate?
2. Is the user authorised to access this endpoint or deployment?

---

## Information to collect

Before escalating, I would collect:

- affected user
- project or team
- endpoint or service URL
- exact error message
- timestamp and timezone
- screenshot if available
- request ID or correlation ID
- whether the issue affects one user or multiple users
- whether other users in the same project can access the endpoint
- recent access changes
- recent deployment or platform changes
- business impact and urgency

---

## First checks

### 1. Confirm scope

Questions:

- Is this affecting one user?
- Is this affecting a whole project team?
- Is this affecting all users?
- Is this only one endpoint or all AI services?

Support value:

Scope helps determine whether the issue is likely user-specific, project-specific or platform-wide.

---

### 2. Confirm authentication vs authorization

If the user can sign in but receives 403, the issue is probably not basic authentication.

Possible causes:

- missing group membership
- missing RBAC role
- wrong project access
- endpoint permission issue
- policy restriction
- application identity has insufficient permission

---

### 3. Compare with a working user

If another user in the same project can access the endpoint, compare:

- group membership
- assigned role
- project access
- endpoint permission
- license or tenant access if relevant

---

### 4. Check for recent changes

Possible recent changes:

- user moved team
- group membership changed
- new model deployment
- endpoint permission changed
- API Management policy changed
- Conditional Access-style policy changed
- pipeline deployed a new configuration

---

## Possible root causes

| Area | Possible cause |
|---|---|
| Identity | User is missing from required group |
| Authorization | RBAC role is missing |
| Platform | Endpoint permission changed |
| API Management | Policy blocks this user or project |
| Deployment | New deployment uses different access settings |
| Process | Access request was not completed correctly |

---

## Escalation note example

User from Project X receives HTTP 403 Forbidden when calling GenAI endpoint Y.

The user can authenticate successfully and access other services, but cannot access this endpoint. Issue started on 2026-05-13 around 09:20 CET. One other user from the same project can access the endpoint successfully.

Collected evidence:

- affected user:
- project:
- endpoint:
- timestamp:
- screenshot:
- request ID:
- business impact:

Initial assessment: this appears to be an authorization issue rather than a full platform outage.

Please review group membership, RBAC and endpoint permissions.

---

## User-facing update

We are investigating an access permission issue affecting your access to the GenAI endpoint.

The service does not currently appear to be fully down. The error suggests that your account or project access may not have the required permissions for this specific endpoint.

We have collected the relevant details and escalated this to the platform / identity team for permission review.

---

## KB improvement after resolution

After resolution, I would update the KB with:

- confirmed root cause
- how to identify similar 403 issues
- required evidence before escalation
- owner team
- known access request process
- examples of good screenshots or request IDs

---

## Interview explanation

In an interview, I would explain this as follows:

A 403 Forbidden error usually means the caller is authenticated but not authorised. I would first confirm scope and impact, collect the endpoint, timestamp, request ID and affected user details, then compare the affected user with a working user if possible.

I would not immediately assume the AI Platform is down. I would investigate whether this is an access, RBAC, group membership, endpoint permission or policy issue.

If the permission change is outside my support scope, I would escalate to the platform or identity team with clear evidence and business impact.

---

## What I would not claim

I would not claim that I would redesign the RBAC model or change production access policies without ownership.

My role would be to support the user, collect evidence, perform first-level analysis, escalate to the correct team and improve the KB after resolution.
