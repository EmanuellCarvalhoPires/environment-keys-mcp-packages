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
path: "/rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}"
category: "Teams in plan"
writes_data: false
tool_note: "[[jira_get_atlassian_team_in_plan]]"
---
# Jira v3 - Get Atlassian team in plan

**Get Atlassian team in plan** — `GET /rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}`

- Run by the tool [[jira_get_atlassian_team_in_plan]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/plans/plan/{{param:planId}}/team/atlassian/{{param:atlassianTeamId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `planId` (path, string, required) — The ID of the plan.
- `atlassianTeamId` (path, string, required) — The ID of the Atlassian team.

## Original description

Returns planning settings for an Atlassian team in a plan.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
