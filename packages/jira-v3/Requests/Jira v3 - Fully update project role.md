---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-roles
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/role/{id}"
category: "Project roles"
writes_data: true
tool_note: "[[jira_fully_update_project_role]]"
---
# Jira v3 - Fully update project role

**Fully update project role** — `PUT /rest/api/3/role/{id}`

- Run by the tool [[jira_fully_update_project_role]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/role/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the project role. Use Get all project roles to get a list of project role IDs.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "A project role that represents developers in a project",
  "name": "Developers"
}
```

## Original description

Updates the project role's name and description. You must include both a name and a description in the request.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
