---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/syncs
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: DELETE
path: "/api/{cloudId}/v1/syncs/{id}"
category: "Syncs"
writes_data: true
---
# JSM Ops - Delete sync

**Delete sync** — `DELETE /api/{cloudId}/v1/syncs/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete sync"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/syncs/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Deletes a sync. 
- The user should have delete permission for sync.
