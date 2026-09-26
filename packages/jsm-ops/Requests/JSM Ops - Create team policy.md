---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/team-policies
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/teams/{teamId}/policies"
category: "Team Policies"
writes_data: true
---
# JSM Ops - Create team policy

**Create team policy** — `POST /api/{cloudId}/v1/teams/{teamId}/policies`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Create team policy"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/policies
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `teamId` (path, string, required) — The jira team identifier
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Create team policy
