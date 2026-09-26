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
path: "/api/{cloudId}/v1/teams/{teamId}/heartbeats"
category: "Heartbeats"
writes_data: false
---
# JSM Ops - List heartbeats

**List heartbeats** — `GET /api/{cloudId}/v1/teams/{teamId}/heartbeats`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List heartbeats"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/heartbeats?name={{param:name}}&offset={{param:offset}}&size={{param:size}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `teamId` (path, string, required) — Identifier of the heartbeat owning team.
- `name` (query, string, optional) — Name of the heartbeat for identification.
- `offset` (query, string, optional) — The offset parameter controls the starting point within the collection of resource results.
- `size` (query, string, optional) — The limit parameter controls the maximum number of items that may be returned for a single request.

## Original description

Lists the all heartbeats user can view. If a heartbeatName is passed, it filters out given heartbeat and only return given heartbeat.
