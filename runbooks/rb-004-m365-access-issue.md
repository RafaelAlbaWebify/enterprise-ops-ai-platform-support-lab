# RB-004 — Microsoft 365 Access Issue

## Purpose

Triage a user who cannot access Microsoft 365 services.

## Symptoms

- Cannot access Teams, SharePoint, OneDrive, Outlook or Office portal
- Access denied
- License-related message
- Sign-in loop
- MFA or Conditional Access-style issue

## Initial checks

1. Confirm user identity.
2. Confirm affected service.
3. Confirm exact error.
4. Check whether issue affects browser, desktop app or both.
5. Check license assignment.
6. Check group membership.
7. Check whether other users are affected.
8. Check Microsoft 365 service health.
9. Collect timestamp, screenshot and device information.

## Likely causes

- License missing
- Group membership issue
- Authentication issue
- Conditional Access-style restriction
- Service incident
- Client cache/session issue

## Escalation

Escalate to identity, Microsoft 365 admin or security team if policy, licensing or tenant-level configuration is suspected.
