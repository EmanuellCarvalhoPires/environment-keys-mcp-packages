---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/team
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/teams/{teamId}/requests/{requestId}"
category: "Team"
writes_data: false
---
# JSM Ops - Get status of a team request

**Get status of a team request** — `GET /api/{cloudId}/v1/teams/{teamId}/requests/{requestId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get status of a team request"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/requests/{{param:requestId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `teamId` (path, string, required) — Value of teamId in the path.
- `requestId` (path, string, required) — ID of the request.

