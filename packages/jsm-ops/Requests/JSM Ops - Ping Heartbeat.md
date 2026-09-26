---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/heartbeats
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/teams/{teamId}/heartbeats/ping"
category: "Heartbeats"
writes_data: false
---
# JSM Ops - Ping Heartbeat

**Ping Heartbeat** — `GET /api/{cloudId}/v1/teams/{teamId}/heartbeats/ping`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Ping Heartbeat"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/heartbeats/ping?name={{param:name}}
Authorization: {{service.auth_token}}
```

## Parameters

- `teamId` (path, string, required) — Identifier of the heartbeat owning team.
- `name` (query, string, required) — Name of the heartbeat for identification.

## Original description

Pings the heartbeat with given name. Heartbeat ping requests processed asynchronously, it does not check if the heartbeat exists or not before responding. Please note that receiving a PONG response does not necessarily mean that the heartbeat exists.
