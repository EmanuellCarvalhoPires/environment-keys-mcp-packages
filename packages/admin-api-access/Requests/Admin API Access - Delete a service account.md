---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/service-account
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Admin API Access]]"
app: "Admin API Access"
method: DELETE
path: "/orgs/{orgId}/service-accounts/{serviceAccountId}"
category: "Service Account"
writes_data: true
---
# Admin API Access - Delete a service account

**Delete a service account** — `DELETE /orgs/{orgId}/service-accounts/{serviceAccountId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Admin API Access - Delete a service account"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/api-access/rest/

```http
DELETE https://api.atlassian.com/admin/api-access/v1/orgs/{{service.org_id}}/service-accounts/{{param:serviceAccountId}}
Authorization: {{service.admin_auth_token}}
```

## Parameters

- `serviceAccountId` (path, string, required) — The unique identifier of the service account to delete.

## Original description

Deletes a service account from the specified organization.

#### Scopes
**[OAuth 2.0 scopes](/cloud/admin/scopes/) required:** `write:service-accounts:admin`
