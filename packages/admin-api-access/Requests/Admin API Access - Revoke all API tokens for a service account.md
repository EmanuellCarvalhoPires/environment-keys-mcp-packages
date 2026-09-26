---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/api-token
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Admin API Access]]"
app: "Admin API Access"
method: DELETE
path: "/orgs/{orgId}/service-accounts/{serviceAccountId}/api-tokens"
category: "API Token"
writes_data: true
---
# Admin API Access - Revoke all API tokens for a service account

**Revoke all API tokens for a service account** — `DELETE /orgs/{orgId}/service-accounts/{serviceAccountId}/api-tokens`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin API Access - Revoke all API tokens for a service account"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/api-access/rest/

```http
DELETE https://api.atlassian.com/admin/api-access/v1/orgs/{{service.org_id}}/service-accounts/{{param:serviceAccountId}}/api-tokens
Authorization: {{service.admin_auth_token}}
```

## Parameters

- `serviceAccountId` (path, string, required) — ID for the service account whose API tokens you want to revoke.

## Original description

Revokes all API tokens for a specific service account within an organization.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `delete:service-accounts-tokens:admin`
