---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/jec
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/jec/action"
category: "JEC"
writes_data: true
---
# JSM Ops - Send JEC Action

**Send JEC Action** — `POST /api/{cloudId}/v1/jec/action`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Send JEC Action"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/jec/action?channelId={{param:channelId}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `channelId` (query, string, optional) — Id of JEC channel.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Send JEC Channel Action
