---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/jec
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/jec/channels"
category: "JEC"
writes_data: true
---
# JSM Ops - Create JEC Channel

**Create JEC Channel** — `POST /api/{cloudId}/v1/jec/channels`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Create JEC Channel"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/jec/channels
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Create JEC Channel
