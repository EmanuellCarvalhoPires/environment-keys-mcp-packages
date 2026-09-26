---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/sync-action-groups
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: PATCH
path: "/api/{cloudId}/v1/syncs/{syncId}/action-groups/{id}"
category: "Sync action groups"
writes_data: true
---
# JSM Ops - Update sync action group

**Update sync action group** — `PATCH /api/{cloudId}/v1/syncs/{syncId}/action-groups/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Update sync action group"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
PATCH https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/syncs/{{param:syncId}}/action-groups/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `syncId` (path, string, required) — Id of the sync
- `id` (path, string, required) — Id of the action group
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates a sync action group.
