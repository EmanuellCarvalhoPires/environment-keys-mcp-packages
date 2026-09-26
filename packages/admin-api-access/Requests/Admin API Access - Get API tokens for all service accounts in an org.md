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
path: "/orgs/{orgId}/service-accounts/api-tokens"
category: "Service Account"
writes_data: false
---
# Admin API Access - Get API tokens for all service accounts in an org

**Get API tokens for all service accounts in an org** — `GET /orgs/{orgId}/service-accounts/api-tokens`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin API Access - Get API tokens for all service accounts in an org"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/api-access/rest/

```http
GET https://api.atlassian.com/admin/api-access/v1/orgs/{{service.org_id}}/service-accounts/api-tokens?tokenLabel={{param:tokenLabel}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `tokenLabel` (query, string, optional) — Optional filter to search for tokens by label.

## Original description

Retrieves API tokens belonging to service accounts in the specified organization.

#### Scopes
**[OAuth 2.0 scopes](/cloud/admin/scopes/) required:** `read:service-accounts-tokens:admin`
