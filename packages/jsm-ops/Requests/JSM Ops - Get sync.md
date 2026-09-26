---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/syncs
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/syncs/{id}"
category: "Syncs"
writes_data: false
---
# JSM Ops - Get sync

**Get sync** — `GET /api/{cloudId}/v1/syncs/{id}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get sync"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/syncs/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Id of the sync.

## Original description

Returns the sync.
