---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/custom-user-roles
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/roles"
category: "Custom user roles"
writes_data: false
---
# JSM Ops - List custom user roles

**List custom user roles** — `GET /api/{cloudId}/v1/roles`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List custom user roles"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/roles?offset={{param:offset}}&size={{param:size}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `offset` (query, string, optional) — Query parameter offset.
- `size` (query, string, optional) — Query parameter size.

## Original description

Returns the list of the custom user roles.  
 - The user should have admin role and custom user role right.
