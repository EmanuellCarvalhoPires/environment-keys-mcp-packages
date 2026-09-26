---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/plans
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/plans/plan/{planId}/duplicate"
category: "Plans"
writes_data: true
tool_note: "[[jira_duplicate_plan]]"
---
# Jira v3 - Duplicate plan

**Duplicate plan** — `POST /rest/api/3/plans/plan/{planId}/duplicate`

- Run by the tool [[jira_duplicate_plan]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/plans/plan/{{param:planId}}/duplicate
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
  "name": "Copied Plan"
}
```

## Original description

Duplicates a plan.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
