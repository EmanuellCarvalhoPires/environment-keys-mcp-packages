---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-role-actors
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/role/{id}/actors"
category: "Project role actors"
writes_data: true
tool_note: "[[jira_add_default_actors_to_project_role]]"
---
# Jira v3 - Add default actors to project role

**Add default actors to project role** — `POST /rest/api/3/role/{id}/actors`

- Run by the tool [[jira_add_default_actors_to_project_role]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/role/{{param:id}}/actors
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
  "user": [
    "admin"
  ]
}
```

## Original description

Adds [default actors](#api-rest-api-3-resolution-get) to a role. You may add groups or users, but you cannot add groups and users in the same request.

Changing a project role's default actors does not affect project role members for projects already created.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
