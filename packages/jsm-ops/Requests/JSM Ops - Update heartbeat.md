---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/heartbeats
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: PATCH
path: "/api/{cloudId}/v1/teams/{teamId}/heartbeats"
category: "Heartbeats"
writes_data: true
---
# JSM Ops - Update heartbeat

**Update heartbeat** — `PATCH /api/{cloudId}/v1/teams/{teamId}/heartbeats`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Update heartbeat"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
PATCH https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/heartbeats?name={{param:name}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `teamId` (path, string, required) — Identifier of the heartbeat owning team.
- `name` (query, string, required) — Name of the heartbeat for identification.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates the heartbeat with the given name. Name of a heartbeat cannot be changed
