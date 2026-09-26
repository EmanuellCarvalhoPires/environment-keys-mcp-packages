---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/custom-user-roles
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/roles"
category: "Custom user roles"
writes_data: true
---
# JSM Ops - Create custom user role

**Create custom user role** — `POST /api/{cloudId}/v1/roles`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Create custom user role"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/roles
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a new custom user role. 
 - The user should have admin role and custom user role right.
