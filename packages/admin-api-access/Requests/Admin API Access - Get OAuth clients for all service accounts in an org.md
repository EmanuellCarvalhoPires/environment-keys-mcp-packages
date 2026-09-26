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
path: "/orgs/{orgId}/service-accounts/oauth-clients"
category: "Service Account"
writes_data: false
---
# Admin API Access - Get OAuth clients for all service accounts in an org

**Get OAuth clients for all service accounts in an org** — `GET /orgs/{orgId}/service-accounts/oauth-clients`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin API Access - Get OAuth clients for all service accounts in an org"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/api-access/rest/

```http
GET https://api.atlassian.com/admin/api-access/v1/orgs/{{service.org_id}}/service-accounts/oauth-clients?clientName={{param:clientName}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `clientName` (query, string, optional) — Optional filter to search for OAuth clients by name.

## Original description

Retrieves OAuth clients belonging to service accounts in the specified organization.

#### Scopes
**[OAuth 2.0 scopes](/cloud/admin/scopes/) required:** `read:service-accounts-tokens:admin`
