---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/policies
  - api/operation/list
  - api/effect/read
up: "[[MCP - Admin Control]]"
app: "Admin Control"
method: GET
path: "/admin/control/v1/orgs/{orgId}/policies"
category: "Policies"
writes_data: false
---
# Admin Control - Get list of policies

**Get list of policies** — `GET /admin/control/v1/orgs/{orgId}/policies`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Control - Get list of policies"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/control/rest/

```http
GET https://api.atlassian.com/admin/control/v1/orgs/{{service.org_id}}/policies?cursor={{param:cursor}}&type={{param:type}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `cursor` (query, string, optional) — Sets the starting point for the page of results to return.
- `type` (query, string, optional) — Sets the type for the page of policies to return.

## Original description

Returns comprehensive details on organizational policies, including both rules and resources.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `read:policies:admin`
