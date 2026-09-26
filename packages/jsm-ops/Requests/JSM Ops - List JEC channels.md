---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/jec
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/jec/channels"
category: "JEC"
writes_data: false
---
# JSM Ops - List JEC channels

**List JEC channels** — `GET /api/{cloudId}/v1/jec/channels`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List JEC channels"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/jec/channels?ownerDomain={{param:ownerDomain}}&size={{param:size}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `ownerDomain` (query, string, optional) — Owner domain of the channel. (For instance, "public")
- `size` (query, string, optional) — The limit parameter controls the maximum number of items that may be returned for a single request.

## Original description

Lists JEC channels according to the provided filters.
- The user should have view permission for JEC
