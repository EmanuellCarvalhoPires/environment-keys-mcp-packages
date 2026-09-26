---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/routing-rules
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/teams/{teamId}/routing-rules"
category: "Routing rules"
writes_data: false
---
# JSM Ops - List routing rules

**List routing rules** — `GET /api/{cloudId}/v1/teams/{teamId}/routing-rules`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List routing rules"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/routing-rules?offset={{param:offset}}&size={{param:size}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `teamId` (path, string, required) — Identifier of the routing rules owning team.
- `offset` (query, string, optional) — The offset parameter controls the starting point within the collection of resource results.
- `size` (query, string, optional) — The limit parameter controls the maximum number of items that may be returned for a single request.

## Original description

Lists all routing rules of given team. It optionally takes two parameters - offset and size.
