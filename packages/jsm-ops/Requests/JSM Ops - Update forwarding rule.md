---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/forwarding-rules
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: PUT
path: "/api/{cloudId}/v1/forwarding-rules/{id}"
category: "Forwarding rules"
writes_data: true
---
# JSM Ops - Update forwarding rule

**Update forwarding rule** — `PUT /api/{cloudId}/v1/forwarding-rules/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Update forwarding rule"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
PUT https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/forwarding-rules/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Identifier of the forwarding rule.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates a forwaring rule with given id in the request.
