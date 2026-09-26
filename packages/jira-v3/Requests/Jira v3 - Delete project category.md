---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-categories
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/projectCategory/{id}"
category: "Project categories"
writes_data: true
tool_note: "[[jira_delete_project_category]]"
---
# Jira v3 - Delete project category

**Delete project category** — `DELETE /rest/api/3/projectCategory/{id}`

- Run by the tool [[jira_delete_project_category]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/projectCategory/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — ID of the project category to delete.

## Original description

Deletes a project category.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
