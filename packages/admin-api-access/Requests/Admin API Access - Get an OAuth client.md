---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/oauth-client
  - api/operation/get
  - api/effect/read
up: "[[MCP - Admin API Access]]"
app: "Admin API Access"
method: GET
path: "/orgs/{orgId}/oauth-clients/{clientId}"
category: "OAuth Client"
writes_data: false
---
# Admin API Access - Get an OAuth client

**Get an OAuth client** — `GET /orgs/{orgId}/oauth-clients/{clientId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin API Access - Get an OAuth client"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/api-access/rest/

```http
GET https://api.atlassian.com/admin/api-access/v1/orgs/{{service.org_id}}/oauth-clients/{{param:clientId}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `clientId` (path, string, required) — The unique identifier of the OAuth client.

## Original description

Retrieves a specific OAuth client by ID for the specified organization.

#### Scopes
**[OAuth 2.0 scopes](/cloud/admin/scopes/) required:** `read:service-accounts-tokens:admin`
