---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/syncs
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/syncs"
category: "Syncs"
writes_data: true
---
# JSM Ops - Create sync

**Create sync** — `POST /api/{cloudId}/v1/syncs`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Create sync"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/syncs
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a sync for syncing alerts created and issues in a selected project. 
- The user should have sync creation permission.
