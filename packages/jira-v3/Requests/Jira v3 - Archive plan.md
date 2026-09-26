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
path: "/rest/api/3/plans/plan/{planId}/archive"
category: "Plans"
writes_data: true
tool_note: "[[jira_archive_plan]]"
---
# Jira v3 - Archive plan

**Archive plan** — `PUT /rest/api/3/plans/plan/{planId}/archive`

- Run by the tool [[jira_archive_plan]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/plans/plan/{{param:planId}}/archive
Authorization: {{service.auth_token}}
```

## Parameters

- `planId` (path, string, required) — The ID of the plan.

## Original description

Archives a plan.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
