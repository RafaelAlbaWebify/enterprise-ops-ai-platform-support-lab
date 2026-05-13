# KB-001 — Authentication vs Authorization

## Authentication

Authentication answers:

> Who are you?

Example:

- User signs in with username, password and MFA.
- API request includes a valid token.
- Application presents a valid managed identity or API key.

## Authorization

Authorization answers:

> What are you allowed to do?

Example:

- User is signed in but does not have access to a resource.
- API token is valid but does not have permission for the endpoint.
- User is not in the required group.

## Common error mapping

| Error | Typical meaning |
|---|---|
| 401 Unauthorized | Authentication problem |
| 403 Forbidden | Authorization problem |

## Support note

A user can authenticate successfully and still receive a 403 if permissions, group membership or RBAC are missing.
