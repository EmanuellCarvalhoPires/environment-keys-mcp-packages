---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-panels
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/forge/panel/action/bulk/async"
category: "Issue panels"
writes_data: true
tool_note: "[[jira_bulk_pin_or_unpin_issue_panel_to_projects]]"
---
# Jira v3 - Bulk pin or unpin issue panel to projects

**Bulk pin or unpin issue panel to projects** — `POST /rest/api/3/forge/panel/action/bulk/async`

- Run by the tool [[jira_bulk_pin_or_unpin_issue_panel_to_projects]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/forge/panel/action/bulk/async
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Bulk pin or unpin an issue panel (added by a Forge app) to or from multiple projects.

The operation runs asynchronously. The response includes a task ID - use the [Get task](#api-rest-api-3-task-taskId-get) endpoint to check progress.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
