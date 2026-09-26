---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/forwarding-rules
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/forwarding-rules"
category: "Forwarding rules"
writes_data: false
---
# JSM Ops - List forwarding rules

**List forwarding rules** — `GET /api/{cloudId}/v1/forwarding-rules`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List forwarding rules"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/forwarding-rules?showAll={{param:showAll}}&offset={{param:offset}}&size={{param:size}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `showAll` (query, string, optional) — Display all forwardings of the account.
- `offset` (query, string, optional) — The offset parameter controls the starting point within the collection of resource results.
- `size` (query, string, optional) — The limit parameter controls the maximum number of items that may be returned for a single request.

## Original description

Lists the all forwarding rules user can view. It optionally takes three parameters - offset, size and showAll.
