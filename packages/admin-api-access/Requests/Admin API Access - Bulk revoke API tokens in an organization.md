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
path: "/orgs/{orgId}/api-tokens"
category: "API Token"
writes_data: true
---
# Admin API Access - Bulk revoke API tokens in an organization

**Bulk revoke API tokens in an organization** — `DELETE /orgs/{orgId}/api-tokens`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin API Access - Bulk revoke API tokens in an organization"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/api-access/rest/

```http
DELETE https://api.atlassian.com/admin/api-access/v1/orgs/{{service.org_id}}/api-tokens
Authorization: {{service.admin_auth_token}}
```

## Original description

Revokes all managed user API tokens in an organization by orgID.
#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `delete:tokens:admin`
