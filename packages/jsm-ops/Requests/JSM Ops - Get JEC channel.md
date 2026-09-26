---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/jec
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/jec/channels/{id}"
category: "JEC"
writes_data: false
---
# JSM Ops - Get JEC channel

**Get JEC channel** — `GET /api/{cloudId}/v1/jec/channels/{id}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get JEC channel"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/jec/channels/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Id of JEC channel.

## Original description

Returns JEC channel
