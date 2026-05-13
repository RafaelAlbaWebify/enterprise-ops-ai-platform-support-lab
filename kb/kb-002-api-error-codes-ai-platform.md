# KB-002 — Common API Error Codes in AI Platform Support

## 400 Bad Request

The request is malformed or contains invalid input.

Support checks:

- Request body
- Required parameters
- Model/deployment name
- Prompt format
- API version

## 401 Unauthorized

The request cannot be authenticated.

Support checks:

- API key
- Token
- Managed identity
- Expired credentials
- Wrong authentication method

## 403 Forbidden

The caller is authenticated but not allowed.

Support checks:

- RBAC
- Group membership
- Endpoint permission
- Project access
- Policy restriction

## 429 Too Many Requests

The service is throttling requests.

Support checks:

- Quota
- Rate limit
- Request volume
- Retry behaviour
- Affected project

## 500 Internal Server Error

The service encountered a server-side problem.

Support checks:

- Service health
- Logs
- Request ID
- Whether multiple users are affected
- Recent deployments
