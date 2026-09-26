---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/domains
  - api/operation/get
  - api/effect/read
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: GET
path: "/v1/orgs/{orgId}/domains/{domainId}"
category: "Domains"
writes_data: false
---
# Admin Orgs - Get domain by ID

**Get domain by ID** — `GET /v1/orgs/{orgId}/domains/{domainId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Orgs - Get domain by ID"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
GET https://api.atlassian.com/admin/v1/orgs/{{service.org_id}}/domains/{{param:domainId}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `domainId` (path, string, required) — ID of the domain to return

## Original description

Returns information about a single verified domain by ID.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `read:domains:admin`
