---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/forwarding-rules
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/forwarding-rules"
category: "Forwarding rules"
writes_data: true
---
# JSM Ops - Create forwarding rule

**Create forwarding rule** — `POST /api/{cloudId}/v1/forwarding-rules`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Create forwarding rule"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/forwarding-rules
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a forwarding rule with the given properties.
