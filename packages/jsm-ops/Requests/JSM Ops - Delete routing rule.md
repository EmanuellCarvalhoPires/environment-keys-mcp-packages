---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/routing-rules
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: DELETE
path: "/api/{cloudId}/v1/teams/{teamId}/routing-rules/{id}"
category: "Routing rules"
writes_data: true
---
# JSM Ops - Delete routing rule

**Delete routing rule** — `DELETE /api/{cloudId}/v1/teams/{teamId}/routing-rules/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete routing rule"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/routing-rules/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `teamId` (path, string, required) — Identifier of the routing rules owning team.
- `id` (path, string, required) — Identifier of the routing rule.

## Original description

Deletes a routing rule with given id in the request.
