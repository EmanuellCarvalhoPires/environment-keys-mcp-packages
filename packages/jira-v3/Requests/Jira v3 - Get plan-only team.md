---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/teams-in-plan
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}"
category: "Teams in plan"
writes_data: false
tool_note: "[[jira_get_plan_only_team]]"
---
# Jira v3 - Get plan-only team

**Get plan-only team** — `GET /rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}`

- Run by the tool [[jira_get_plan_only_team]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/plans/plan/{{param:planId}}/team/planonly/{{param:planOnlyTeamId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `planId` (path, string, required) — The ID of the plan.
- `planOnlyTeamId` (path, string, required) — The ID of the plan-only team.

## Original description

Returns planning settings for a plan-only team.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
