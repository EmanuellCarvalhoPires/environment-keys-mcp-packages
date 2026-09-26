---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-role-actors
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/project/{projectIdOrKey}/role/{id}"
category: "Project role actors"
writes_data: true
tool_note: "[[jira_add_actors_to_project_role]]"
---
# Jira v3 - Add actors to project role

**Add actors to project role** — `POST /rest/api/3/project/{projectIdOrKey}/role/{id}`

- Run by the tool [[jira_add_actors_to_project_role]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/role/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project ID or project key (case sensitive).
- `id` (path, string, required) — The ID of the project role. Use Get all project roles to get a list of project role IDs.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "groupId": [
    "952d12c3-5b5b-4d04-bb32-44d383afc4b2"
  ]
}
```

## Original description

Adds actors to a project role for the project.

To replace all actors for the project, use [Set actors for project role](#api-rest-api-3-project-projectIdOrKey-role-id-put).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
