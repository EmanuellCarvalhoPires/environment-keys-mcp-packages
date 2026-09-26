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
path: "/rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}"
category: "Teams in plan"
writes_data: true
tool_note: "[[jira_delete_plan_only_team]]"
---
# Jira v3 - Delete plan-only team

**Delete plan-only team** — `DELETE /rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}`

- Run by the tool [[jira_delete_plan_only_team]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/plans/plan/{{param:planId}}/team/planonly/{{param:planOnlyTeamId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `planId` (path, string, required) — The ID of the plan.
- `planOnlyTeamId` (path, string, required) — The ID of the plan-only team.

## Original description

Deletes a plan-only team and their planning settings.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
