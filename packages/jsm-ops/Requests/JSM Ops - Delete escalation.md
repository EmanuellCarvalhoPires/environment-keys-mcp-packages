---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/escalations
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: DELETE
path: "/api/{cloudId}/v1/teams/{teamId}/escalations/{id}"
category: "Escalations"
writes_data: true
---
# JSM Ops - Delete escalation

**Delete escalation** — `DELETE /api/{cloudId}/v1/teams/{teamId}/escalations/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete escalation"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/escalations/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `teamId` (path, string, required) — Identifer of the escalation owning team.
- `id` (path, string, required) — Identifier of the escalation.

## Original description

Deletes an escalation with given id in the request.
