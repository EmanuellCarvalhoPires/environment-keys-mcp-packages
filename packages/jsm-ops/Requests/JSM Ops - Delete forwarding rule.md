---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/forwarding-rules
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: DELETE
path: "/api/{cloudId}/v1/forwarding-rules/{id}"
category: "Forwarding rules"
writes_data: true
---
# JSM Ops - Delete forwarding rule

**Delete forwarding rule** — `DELETE /api/{cloudId}/v1/forwarding-rules/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete forwarding rule"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/forwarding-rules/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Identifier of the forwarding rule.

## Original description

Deletes a forwarding rule with given id in the request.
