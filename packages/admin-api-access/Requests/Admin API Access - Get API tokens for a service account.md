---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/service-account
  - api/operation/list
  - api/effect/read
up: "[[MCP - Admin API Access]]"
app: "Admin API Access"
method: GET
path: "/orgs/{orgId}/service-accounts/{serviceAccountId}/api-tokens"
category: "Service Account"
writes_data: false
---
# Admin API Access - Get API tokens for a service account

**Get API tokens for a service account** — `GET /orgs/{orgId}/service-accounts/{serviceAccountId}/api-tokens`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin API Access - Get API tokens for a service account"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/api-access/rest/

```http
GET https://api.atlassian.com/admin/api-access/v1/orgs/{{service.org_id}}/service-accounts/{{param:serviceAccountId}}/api-tokens?tokenLabel={{param:tokenLabel}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `serviceAccountId` (path, string, required) — ID for the service account whose API tokens you want to retrieve.
- `tokenLabel` (query, string, optional) — Optional filter to search for tokens by label.

## Original description

Retrieves API tokens for a specific service account within an organization.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `read:service-accounts-tokens:admin`
