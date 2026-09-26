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
path: "/rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}"
category: "Teams in plan"
writes_data: true
tool_note: "[[jira_update_plan_only_team]]"
---
# Jira v3 - Update plan-only team

**Update plan-only team** — `PUT /rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}`

- Run by the tool [[jira_update_plan_only_team]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/plans/plan/{{param:planId}}/team/planonly/{{param:planOnlyTeamId}}
Authorization: {{service.auth_token}}
Content-Type: application/json-patch+json

{{param:body}}
```

## Parameters

- `planId` (path, string, required) — The ID of the plan.
- `planOnlyTeamId` (path, string, required) — The ID of the plan-only team.
- `body` (body, array, required) — JSON request body. See the example in the request note.

## Body (example)

```json
[{"op": "replace", "path": "/planningStyle", "value": "Kanban"}]
```

## Original description

Updates any of the following planning settings of a plan-only team using [JSON Patch](https://datatracker.ietf.org/doc/html/rfc6902).

 *  name
 *  planningStyle
 *  issueSourceId
 *  sprintLength
 *  capacity
 *  memberAccountIds

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

*Note that "add" operations do not respect array indexes in target locations. Call the "Get plan-only team" endpoint to find out the order of array elements.*
