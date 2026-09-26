---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/projects
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/project/{projectIdOrKey}/delete"
category: "Projects"
writes_data: true
tool_note: "[[jira_delete_project_asynchronously]]"
---
# Jira v3 - Delete project asynchronously

**Delete project asynchronously** — `POST /rest/api/3/project/{projectIdOrKey}/delete`

- Run by the tool [[jira_delete_project_asynchronously]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/delete
Authorization: {{service.auth_token}}
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project ID or project key (case sensitive).

## Original description

Deletes a project asynchronously.

This operation is:

 *  transactional, that is, if part of the delete fails the project is not deleted.
 *  [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
