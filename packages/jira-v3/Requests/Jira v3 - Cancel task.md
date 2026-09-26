---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/tasks
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/task/{taskId}/cancel"
category: "Tasks"
writes_data: true
tool_note: "[[jira_cancel_task]]"
---
# Jira v3 - Cancel task

**Cancel task** — `POST /rest/api/3/task/{taskId}/cancel`

- Run by the tool [[jira_cancel_task]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/task/{{param:taskId}}/cancel
Authorization: {{service.auth_token}}
```

## Parameters

- `taskId` (path, string, required) — The ID of the task.

## Original description

Cancels a task.

**[Permissions](#permissions) required:** either of:

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
 *  Creator of the task.
