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
path: "/orgs/{orgId}/service-accounts/{serviceAccountId}/oauth-clients"
category: "Service Account"
writes_data: false
---
# Admin API Access - Get OAuth clients for a service account

**Get OAuth clients for a service account** — `GET /orgs/{orgId}/service-accounts/{serviceAccountId}/oauth-clients`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin API Access - Get OAuth clients for a service account"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/api-access/rest/

```http
GET https://api.atlassian.com/admin/api-access/v1/orgs/{{service.org_id}}/service-accounts/{{param:serviceAccountId}}/oauth-clients?clientName={{param:clientName}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `serviceAccountId` (path, string, required) — ID for the service account whose OAuth clients you want to retrieve.
- `clientName` (query, string, optional) — Optional filter to search for OAuth clients by name.

## Original description

Retrieves OAuth clients belonging to the specified service account.

#### Scopes
**[OAuth 2.0 scopes](/cloud/admin/scopes/) required:** `read:service-accounts-tokens:admin`
