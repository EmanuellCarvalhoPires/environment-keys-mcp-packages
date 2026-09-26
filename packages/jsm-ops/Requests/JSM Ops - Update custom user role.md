---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/custom-user-roles
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: PUT
path: "/api/{cloudId}/v1/roles/{identifier}"
category: "Custom user roles"
writes_data: true
---
# JSM Ops - Update custom user role

**Update custom user role** — `PUT /api/{cloudId}/v1/roles/{identifier}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Update custom user role"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
PUT https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/roles/{{param:identifier}}?identifierType={{param:identifierType}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `identifier` (path, string, required) — Id of the custom user role.
- `identifierType` (query, string, optional) — Type of the identifier.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates the details of a custom user role. 
 - The user should have admin role and custom user role right.
