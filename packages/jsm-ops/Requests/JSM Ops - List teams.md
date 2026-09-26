---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/team
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/teams"
category: "Team"
writes_data: false
---
# JSM Ops - List teams

**List teams** — `GET /api/{cloudId}/v1/teams`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List teams"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Lists operations teams based on the user's role. If the user has admin rights, all teams are listed; otherwise, only the teams the user is a member of are shown.
