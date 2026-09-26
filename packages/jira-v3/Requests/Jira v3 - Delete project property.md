---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-properties
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}"
category: "Project properties"
writes_data: true
tool_note: "[[jira_delete_project_property]]"
---
# Jira v3 - Delete project property

**Delete project property** — `DELETE /rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}`

- Run by the tool [[jira_delete_project_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project ID or project key (case sensitive).
- `propertyKey` (path, string, required) — The project property key. Use Get project property keys to get a list of all project property keys.

## Original description

Deletes the [property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties) from a project.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the property.
