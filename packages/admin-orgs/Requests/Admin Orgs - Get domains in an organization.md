---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/domains
  - api/operation/list
  - api/effect/read
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: GET
path: "/v1/orgs/{orgId}/domains"
category: "Domains"
writes_data: false
---
# Admin Orgs - Get domains in an organization

**Get domains in an organization** — `GET /v1/orgs/{orgId}/domains`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Orgs - Get domains in an organization"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
GET https://api.atlassian.com/admin/v1/orgs/{{service.org_id}}/domains?cursor={{param:cursor}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `cursor` (query, string, optional) — Sets the starting point for the page of results to return.

## Original description

Returns a list of domains in an organization one page at a time.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `read:domains:admin`
