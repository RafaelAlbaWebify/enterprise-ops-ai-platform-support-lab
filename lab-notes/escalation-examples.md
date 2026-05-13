# Escalation Examples

## Good escalation: AI Platform 403

User from Project A receives 403 Forbidden when calling endpoint X. Authentication appears successful. Issue started at 09:20 CET. Other users in the same project can access the endpoint. Request ID and screenshot attached. Please review RBAC or group membership for this user.

## Good escalation: Pipeline failure

Pipeline Y failed on branch main at deployment stage. Build completed successfully. Failed task: Deploy to test environment. Error suggests missing variable or permission. No production impact. Please review deployment configuration.

## Poor escalation

AI is broken. Please check.

## Why it is poor

- No user
- No timestamp
- No error
- No impact
- No request ID
- No troubleshooting evidence
