---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/teams-in-plan
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/plans/plan/{planId}/team/atlassian"
category: "Teams in plan"
writes_data: true
tool_note: "[[jira_add_atlassian_team_to_plan]]"
---
# Jira v3 - Add Atlassian team to plan

**Add Atlassian team to plan** — `POST /rest/api/3/plans/plan/{planId}/team/atlassian`

- Run by the tool [[jira_add_atlassian_team_to_plan]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/plans/plan/{{param:planId}}/team/atlassian
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `planId` (path, string, required) — The ID of the plan.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "capacity": 200,
  "id": "AtlassianTeamId",
  "issueSourceId": 0,
  "planningStyle": "Scrum",
  "sprintLength": 2
}
```

## Original description

Adds an existing Atlassian team to a plan and configures their plannning settings.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
