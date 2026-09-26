---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/team-policies
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/teams/{teamId}/policies"
category: "Team Policies"
writes_data: false
---
# JSM Ops - List team policies

**List team policies** — `GET /api/{cloudId}/v1/teams/{teamId}/policies`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List team policies"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/policies?type={{param:type}}&size={{param:size}}&offset={{param:offset}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `teamId` (path, string, required) — The jira team identifier
- `type` (query, string, required) — The type of policy. alert or notification
- `size` (query, string, optional) — The limit parameter controls the maximum number of items that may be returned for a single request.
- `offset` (query, string, optional) — The offset parameter controls the starting point within the collection of resource results.

## Original description

List team policies
