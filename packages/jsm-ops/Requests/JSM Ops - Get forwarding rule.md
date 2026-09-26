---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/forwarding-rules
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/forwarding-rules/{id}"
category: "Forwarding rules"
writes_data: false
---
# JSM Ops - Get forwarding rule

**Get forwarding rule** — `GET /api/{cloudId}/v1/forwarding-rules/{id}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get forwarding rule"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/forwarding-rules/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Identifier of the forwarding rule.

## Original description

Gets a forwarding rule with given id in the request.
