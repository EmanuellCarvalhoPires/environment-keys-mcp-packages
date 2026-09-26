---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/tasks
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/task/{taskId}"
category: "Tasks"
writes_data: false
tool_note: "[[jira_get_task]]"
---
# Jira v3 - Get task

**Get task** — `GET /rest/api/3/task/{taskId}`

- Run by the tool [[jira_get_task]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/task/{{param:taskId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `taskId` (path, string, required) — The ID of the task.

## Original description

Returns the status of a [long-running asynchronous task](#async).

When a task has finished, this operation returns the JSON blob applicable to the task. See the documentation of the operation that created the task for details. Task details are not permanently retained. As of September 2019, details are retained for 14 days although this period may change without notice.

**Deprecation notice:** The required OAuth 2.0 scopes will be updated on June 15, 2024.

 *  `read:jira-work`

**[Permissions](#permissions) required:** either of:

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
 *  Creator of the task.
