---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/sync-actions
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: DELETE
path: "/api/{cloudId}/v1/syncs/{syncId}/actions/{id}"
category: "Sync actions"
writes_data: true
---
# JSM Ops - Delete sync action

**Delete sync action** — `DELETE /api/{cloudId}/v1/syncs/{syncId}/actions/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete sync action"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/syncs/{{param:syncId}}/actions/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `syncId` (path, string, required) — Id of the sync.
- `id` (path, string, required) — Id of the sync action.

## Original description

Deletes a sync action.
