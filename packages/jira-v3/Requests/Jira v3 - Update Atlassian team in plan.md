---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/teams-in-plan
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}"
category: "Teams in plan"
writes_data: true
tool_note: "[[jira_update_atlassian_team_in_plan]]"
---
# Jira v3 - Update Atlassian team in plan

**Update Atlassian team in plan** — `PUT /rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}`

- Run by the tool [[jira_update_atlassian_team_in_plan]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/plans/plan/{{param:planId}}/team/atlassian/{{param:atlassianTeamId}}
Authorization: {{service.auth_token}}
Content-Type: application/json-patch+json

{{param:body}}
```

## Parameters

- `planId` (path, string, required) — The ID of the plan.
- `atlassianTeamId` (path, string, required) — The ID of the Atlassian team.
- `body` (body, array, required) — JSON request body. See the example in the request note.

## Body (example)

```json
[{"op": "replace", "path": "/planningStyle", "value": "Kanban"}]
```

## Original description

Updates any of the following planning settings of an Atlassian team in a plan using [JSON Patch](https://datatracker.ietf.org/doc/html/rfc6902).

 *  planningStyle
 *  issueSourceId
 *  sprintLength
 *  capacity

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

*Note that "add" operations do not respect array indexes in target locations. Call the "Get Atlassian team in plan" endpoint to find out the order of array elements.*
