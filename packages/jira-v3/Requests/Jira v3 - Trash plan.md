---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/plans
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/plans/plan/{planId}/trash"
category: "Plans"
writes_data: true
tool_note: "[[jira_trash_plan]]"
---
# Jira v3 - Trash plan

**Trash plan** — `PUT /rest/api/3/plans/plan/{planId}/trash`

- Run by the tool [[jira_trash_plan]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/plans/plan/{{param:planId}}/trash
Authorization: {{service.auth_token}}
```

## Parameters

- `planId` (path, string, required) — The ID of the plan.

## Original description

Moves a plan to trash.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
