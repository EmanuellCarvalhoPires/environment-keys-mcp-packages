---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/custom-user-roles
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/roles/{identifier}"
category: "Custom user roles"
writes_data: false
---
# JSM Ops - Get custom user role

**Get custom user role** — `GET /api/{cloudId}/v1/roles/{identifier}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get custom user role"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/roles/{{param:identifier}}?identifierType={{param:identifierType}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `identifier` (path, string, required) — Id of the custom user role.
- `identifierType` (query, string, optional) — Type of the identifier.

## Original description

Returns details of a custom user role. 
 - The user should have admin role and custom user role right.
