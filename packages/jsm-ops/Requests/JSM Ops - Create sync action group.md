---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/sync-action-groups
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/syncs/{syncId}/action-groups"
category: "Sync action groups"
writes_data: true
---
# JSM Ops - Create sync action group

**Create sync action group** — `POST /api/{cloudId}/v1/syncs/{syncId}/action-groups`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Create sync action group"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/syncs/{{param:syncId}}/action-groups
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `syncId` (path, string, required) — Id of the sync
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a sync action group
