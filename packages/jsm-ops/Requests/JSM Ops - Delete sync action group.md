---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/sync-action-groups
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: DELETE
path: "/api/{cloudId}/v1/syncs/{syncId}/action-groups/{id}"
category: "Sync action groups"
writes_data: true
---
# JSM Ops - Delete sync action group

**Delete sync action group** — `DELETE /api/{cloudId}/v1/syncs/{syncId}/action-groups/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete sync action group"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/syncs/{{param:syncId}}/action-groups/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `syncId` (path, string, required) — Id of the sync
- `id` (path, string, required) — Id of the action group

## Original description

Deletes a sync action group.
