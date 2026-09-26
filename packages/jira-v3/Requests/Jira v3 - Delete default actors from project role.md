---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-role-actors
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/role/{id}/actors"
category: "Project role actors"
writes_data: true
tool_note: "[[jira_delete_default_actors_from_project_role]]"
---
# Jira v3 - Delete default actors from project role

**Delete default actors from project role** — `DELETE /rest/api/3/role/{id}/actors`

- Run by the tool [[jira_delete_default_actors_from_project_role]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/role/{{param:id}}/actors?user={{param:user}}&groupId={{param:groupId}}&group={{param:group}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the project role. Use Get all project roles to get a list of project role IDs.
- `user` (query, string, optional) — The user account ID of the user to remove as a default actor.
- `groupId` (query, string, optional) — The group ID of the group to be removed as a default actor. This parameter cannot be used with the group parameter.
- `group` (query, string, optional) — The group name of the group to be removed as a default actor.This parameter cannot be used with the groupId parameter. As a group's name can change, use of groupId is recommended.

## Original description

Deletes the [default actors](#api-rest-api-3-resolution-get) from a project role. You may delete a group or user, but you cannot delete a group and a user in the same request.

Changing a project role's default actors does not affect project role members for projects already created.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
