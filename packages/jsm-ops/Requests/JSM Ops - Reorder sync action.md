---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/sync-actions
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: PATCH
path: "/api/{cloudId}/v1/syncs/{syncId}/actions/{id}/order"
category: "Sync actions"
writes_data: true
---
# JSM Ops - Reorder sync action

**Reorder sync action** — `PATCH /api/{cloudId}/v1/syncs/{syncId}/actions/{id}/order`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Reorder sync action"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
PATCH https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/syncs/{{param:syncId}}/actions/{{param:id}}/order
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `syncId` (path, string, required) — Id of the sync.
- `id` (path, string, required) — Id of the sync action.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Reorders a sync action.
