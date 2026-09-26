---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/sync-actions
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/syncs/{syncId}/actions/{id}"
category: "Sync actions"
writes_data: false
---
# JSM Ops - Get sync action

**Get sync action** — `GET /api/{cloudId}/v1/syncs/{syncId}/actions/{id}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get sync action"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/syncs/{{param:syncId}}/actions/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `syncId` (path, string, required) — Id of the sync.
- `id` (path, string, required) — Id of the sync action.

## Original description

Gets a sync action.
