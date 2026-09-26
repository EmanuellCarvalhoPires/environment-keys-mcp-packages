---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/policies
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/alerts/policies"
category: "Policies"
writes_data: false
---
# JSM Ops - List global alert policies

**List global alert policies** — `GET /api/{cloudId}/v1/alerts/policies`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List global alert policies"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/policies?offset={{param:offset}}&size={{param:size}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `offset` (query, string, optional) — The offset parameter controls the starting point within the collection of resource results.
- `size` (query, string, optional) — The limit parameter controls the maximum number of items that may be returned for a single request.

## Original description

List global alert policies
