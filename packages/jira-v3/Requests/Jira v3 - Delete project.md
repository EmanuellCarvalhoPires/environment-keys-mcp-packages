---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/projects
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/project/{projectIdOrKey}"
category: "Projects"
writes_data: true
tool_note: "[[jira_delete_project]]"
---
# Jira v3 - Delete project

**Delete project** — `DELETE /rest/api/3/project/{projectIdOrKey}`

- Run by the tool [[jira_delete_project]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}?enableUndo={{param:enableUndo}}
Authorization: {{service.auth_token}}
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project ID or project key (case sensitive).
- `enableUndo` (query, string, optional) — Whether this project is placed in the Jira recycle bin where it will be available for restoration.

## Original description

Deletes a project.

You can't delete a project if it's archived. To delete an archived project, restore the project and then delete it. To restore a project, use the Jira UI.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
