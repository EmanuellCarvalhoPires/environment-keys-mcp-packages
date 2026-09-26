---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/policies
  - api/operation/list
  - api/effect/read
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: GET
path: "/v1/orgs/{orgId}/policies"
category: "Policies"
writes_data: false
---
# Admin Orgs - Get list of policies

**Get list of policies** — `GET /v1/orgs/{orgId}/policies`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Orgs - Get list of policies"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
GET https://api.atlassian.com/admin/v1/orgs/{{service.org_id}}/policies?cursor={{param:cursor}}&type={{param:type}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `cursor` (query, string, optional) — Sets the starting point for the page of results to return.
- `type` (query, string, optional) — Sets the type for the page of policies to return.

## Original description

Returns information about org policies
