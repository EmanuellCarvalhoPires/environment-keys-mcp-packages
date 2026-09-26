---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-roles
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/role/{id}"
category: "Project roles"
writes_data: true
tool_note: "[[jira_delete_project_role]]"
---
# Jira v3 - Delete project role

**Delete project role** — `DELETE /rest/api/3/role/{id}`

- Run by the tool [[jira_delete_project_role]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/role/{{param:id}}?swap={{param:swap}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the project role to delete. Use Get all project roles to get a list of project role IDs.
- `swap` (query, string, optional) — The ID of the project role that will replace the one being deleted. The swap will attempt to swap the role in schemes (notifications, permissions, issue security), workflows, worklogs and comments.

## Original description

Deletes a project role. You must specify a replacement project role if you wish to delete a project role that is in use.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
