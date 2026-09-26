---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/teams-in-plan
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/plans/plan/{planId}/team"
category: "Teams in plan"
writes_data: false
tool_note: "[[jira_get_teams_in_plan_paginated]]"
---
# Jira v3 - Get teams in plan paginated

**Get teams in plan paginated** — `GET /rest/api/3/plans/plan/{planId}/team`

- Run by the tool [[jira_get_teams_in_plan_paginated]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/plans/plan/{{param:planId}}/team?cursor={{param:cursor}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `planId` (path, string, required) — The ID of the plan.
- `cursor` (query, string, optional) — The cursor to start from. If not provided, the first page will be returned.
- `maxResults` (query, string, optional) — The maximum number of plan teams to return per page. The maximum value is 50. The default value is 50.

## Original description

Returns a [paginated](#pagination) list of plan-only and Atlassian teams in a plan.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
