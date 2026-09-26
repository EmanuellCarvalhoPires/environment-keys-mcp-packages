---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/heartbeats
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: DELETE
path: "/api/{cloudId}/v1/teams/{teamId}/heartbeats"
category: "Heartbeats"
writes_data: true
---
# JSM Ops - Delete heartbeat

**Delete heartbeat** — `DELETE /api/{cloudId}/v1/teams/{teamId}/heartbeats`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete heartbeat"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/heartbeats?name={{param:name}}
Authorization: {{service.auth_token}}
```

## Parameters

- `teamId` (path, string, required) — Identifier of the heartbeat owning team.
- `name` (query, string, required) — Name of the heartbeat for identification.

## Original description

Deletes the heartbeat with given name in the request.
