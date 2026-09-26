---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-components
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/component/{id}"
category: "Project components"
writes_data: true
tool_note: "[[jira_delete_component]]"
---
# Jira v3 - Delete component

**Delete component** — `DELETE /rest/api/3/component/{id}`

- Run by the tool [[jira_delete_component]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/component/{{param:id}}?moveIssuesTo={{param:moveIssuesTo}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the component.
- `moveIssuesTo` (query, string, optional) — The ID of the component to replace the deleted component. If this value is null no replacement is made.

## Original description

Deletes a component.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the component or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
