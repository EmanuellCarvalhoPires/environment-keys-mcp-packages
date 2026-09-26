---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/jec
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: DELETE
path: "/api/{cloudId}/v1/jec/channels/{id}"
category: "JEC"
writes_data: true
---
# JSM Ops - Delete JEC channel

**Delete JEC channel** — `DELETE /api/{cloudId}/v1/jec/channels/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete JEC channel"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/jec/channels/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Id of JEC channel.

## Original description

Delete JEC channel
