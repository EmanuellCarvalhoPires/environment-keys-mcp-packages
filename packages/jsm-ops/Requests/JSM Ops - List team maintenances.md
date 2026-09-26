---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/maintenances
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/teams/{teamId}/maintenances"
category: "Maintenances"
writes_data: false
---
# JSM Ops - List team maintenances

**List team maintenances** — `GET /api/{cloudId}/v1/teams/{teamId}/maintenances`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List team maintenances"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/maintenances?type={{param:type}}&offset={{param:offset}}&size={{param:size}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `teamId` (path, string, required) — Identifier of the maintenance owning team.
- `type` (query, string, optional) — Defines which maintenance will be listed according to maintenance status.
- `offset` (query, string, optional) — The offset parameter controls the starting point within the collection of resource results.
- `size` (query, string, optional) — The limit parameter controls the maximum number of items that may be returned for a single request.

## Original description

This endpoint is used to retrieve a list of maintenance associated with a specific team in the Jira Service Management system. It optionally takes three parameters - offset, size and type.
