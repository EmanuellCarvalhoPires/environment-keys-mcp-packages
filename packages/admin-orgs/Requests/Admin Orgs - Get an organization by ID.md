---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/orgs
  - api/operation/list
  - api/effect/read
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: GET
path: "/v1/orgs/{orgId}"
category: "Orgs"
writes_data: false
---
# Admin Orgs - Get an organization by ID

**Get an organization by ID** — `GET /v1/orgs/{orgId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Orgs - Get an organization by ID"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
GET https://api.atlassian.com/admin/v1/orgs/{{service.org_id}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Original description

Returns information about a single organization by ID

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `read:orgs:admin`
