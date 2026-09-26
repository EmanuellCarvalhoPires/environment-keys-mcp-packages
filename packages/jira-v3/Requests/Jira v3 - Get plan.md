---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/plans
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/plans/plan/{planId}"
category: "Plans"
writes_data: false
tool_note: "[[jira_get_plan]]"
---
# Jira v3 - Get plan

**Get plan** — `GET /rest/api/3/plans/plan/{planId}`

- Run by the tool [[jira_get_plan]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/plans/plan/{{param:planId}}?useGroupId={{param:useGroupId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `planId` (path, string, required) — The ID of the plan.
- `useGroupId` (query, string, optional) — Whether to return group IDs instead of group names. Group names are deprecated.

## Original description

Returns a plan.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
