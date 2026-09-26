---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-role-actors
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/project/{projectIdOrKey}/role/{id}"
category: "Project role actors"
writes_data: true
tool_note: "[[jira_set_actors_for_project_role]]"
---
# Jira v3 - Set actors for project role

**Set actors for project role** — `PUT /rest/api/3/project/{projectIdOrKey}/role/{id}`

- Run by the tool [[jira_set_actors_for_project_role]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/role/{{param:id}}
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
  "categorisedActors": {
    "atlassian-group-role-actor-id": [
      "952d12c3-5b5b-4d04-bb32-44d383afc4b2"
    ],
    "atlassian-user-role-actor": [
      "12345678-9abc-def1-2345-6789abcdef12"
    ]
  }
}
```

## Original description

Sets the actors for a project role for a project, replacing all existing actors.

To add actors to the project without overwriting the existing list, use [Add actors to project role](#api-rest-api-3-project-projectIdOrKey-role-id-post).

**[Permissions](#permissions) required:** *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
