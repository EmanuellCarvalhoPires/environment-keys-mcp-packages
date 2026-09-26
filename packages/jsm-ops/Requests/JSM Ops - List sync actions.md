---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/sync-actions
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/syncs/{syncId}/actions"
category: "Sync actions"
writes_data: false
---
# JSM Ops - List sync actions

**List sync actions** — `GET /api/{cloudId}/v1/syncs/{syncId}/actions`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List sync actions"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/syncs/{{param:syncId}}/actions?type={{param:type}}&direction={{param:direction}}&groupId={{param:groupId}}&name={{param:name}}&offset={{param:offset}}&size={{param:size}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `syncId` (path, string, required) — Value of syncId in the path.
- `type` (query, string, optional) — Type of the action.
- `direction` (query, string, optional) — Direction of the action.
- `groupId` (query, string, optional) — Id of the action group that the action belongs to.
- `name` (query, string, optional) — Name of the action.
- `offset` (query, string, optional) — The offset parameter controls the starting point within the collection of resource results.
- `size` (query, string, optional) — The limit parameter controls the maximum number of items that may be returned for a single request.

## Original description

Lists sync actions of a sync
