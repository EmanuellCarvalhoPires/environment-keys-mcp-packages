---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/escalations
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/teams/{teamId}/escalations"
category: "Escalations"
writes_data: false
---
# JSM Ops - List escalations

**List escalations** — `GET /api/{cloudId}/v1/teams/{teamId}/escalations`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List escalations"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/escalations?offset={{param:offset}}&size={{param:size}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `teamId` (path, string, required) — Identifier of the escalation owning team.
- `offset` (query, string, optional) — The offset parameter controls the starting point within the collection of resource results.
- `size` (query, string, optional) — The limit parameter controls the maximum number of items that may be returned for a single request.

## Original description

Lists all escalations under given team. It optionally takes two parameters - offset and size.
