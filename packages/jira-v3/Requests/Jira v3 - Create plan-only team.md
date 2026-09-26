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
path: "/rest/api/3/plans/plan/{planId}/team/planonly"
category: "Teams in plan"
writes_data: true
tool_note: "[[jira_create_plan_only_team]]"
---
# Jira v3 - Create plan-only team

**Create plan-only team** — `POST /rest/api/3/plans/plan/{planId}/team/planonly`

- Run by the tool [[jira_create_plan_only_team]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/plans/plan/{{param:planId}}/team/planonly
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
  "issueSourceId": 0,
  "memberAccountIds": [
    "member1AccountId",
    "member2AccountId"
  ],
  "name": "Team1",
  "planningStyle": "Scrum",
  "sprintLength": 2
}
```

## Original description

Creates a plan-only team and configures their planning settings.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
