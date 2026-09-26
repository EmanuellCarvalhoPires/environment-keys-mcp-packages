---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/heartbeats
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/teams/{teamId}/heartbeats"
category: "Heartbeats"
writes_data: true
---
# JSM Ops - Create heartbeat

**Create heartbeat** — `POST /api/{cloudId}/v1/teams/{teamId}/heartbeats`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Create heartbeat"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/heartbeats
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `teamId` (path, string, required) — Identifier of the heartbeat owning team.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Create heartbeat request is used to define heartbeats in Jira Service Management. A heartbeat needs to be added, before sending heartbeat messages to JSM
