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
path: "/v1/orgs"
category: "Orgs"
writes_data: false
---
# Admin Orgs - Get organizations

**Get organizations** — `GET /v1/orgs`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Orgs - Get organizations"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
GET https://api.atlassian.com/admin/v1/orgs?cursor={{param:cursor}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `cursor` (query, string, optional) — Sets the starting point for the page of results to return.

## Original description

Returns a list of your organizations (based on your API key).
