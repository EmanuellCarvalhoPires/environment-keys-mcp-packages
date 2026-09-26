---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-resolutions
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/resolution/{id}"
category: "Issue resolutions"
writes_data: true
tool_note: "[[jira_delete_resolution]]"
---
# Jira v3 - Delete resolution

**Delete resolution** — `DELETE /rest/api/3/resolution/{id}`

- Run by the tool [[jira_delete_resolution]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/resolution/{{param:id}}?replaceWith={{param:replaceWith}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the issue resolution.
- `replaceWith` (query, string, required) — The ID of the issue resolution that will replace the currently selected resolution.

## Original description

Deletes an issue resolution.

This operation is [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
