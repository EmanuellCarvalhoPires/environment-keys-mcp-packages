---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/api-key
  - api/operation/update
  - api/effect/write
up: "[[MCP - Admin API Access]]"
app: "Admin API Access"
method: PATCH
path: "/orgs/{orgId}/api-keys/revoke/{apiKeyId}"
category: "API Key"
writes_data: true
---
# Admin API Access - Revoke an API key for an org

**Revoke an API key for an org** — `PATCH /orgs/{orgId}/api-keys/revoke/{apiKeyId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin API Access - Revoke an API key for an org"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/api-access/rest/

```http
PATCH https://api.atlassian.com/admin/api-access/v1/orgs/{{service.org_id}}/api-keys/revoke/{{param:apiKeyId}}
Authorization: {{service.admin_auth_token}}
```

## Parameters

- `apiKeyId` (path, string, required) — ID for the API key you want to revoke.

## Original description

Revokes an existing API key

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `delete:keys:admin`
