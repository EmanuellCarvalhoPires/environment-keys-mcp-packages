---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/teams-in-plan
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}"
category: "Teams in plan"
writes_data: true
tool_note: "[[jira_remove_atlassian_team_from_plan]]"
---
# Jira v3 - Remove Atlassian team from plan

**Remove Atlassian team from plan** — `DELETE /rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}`

- Run by the tool [[jira_remove_atlassian_team_from_plan]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/plans/plan/{{param:planId}}/team/atlassian/{{param:atlassianTeamId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `planId` (path, string, required) — The ID of the plan.
- `atlassianTeamId` (path, string, required) — The ID of the Atlassian team.

## Original description

Removes an Atlassian team from a plan and deletes their planning settings.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
