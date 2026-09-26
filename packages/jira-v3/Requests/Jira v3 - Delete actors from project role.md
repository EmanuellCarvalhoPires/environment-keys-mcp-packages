---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-role-actors
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/project/{projectIdOrKey}/role/{id}"
category: "Project role actors"
writes_data: true
tool_note: "[[jira_delete_actors_from_project_role]]"
---
# Jira v3 - Delete actors from project role

**Delete actors from project role** — `DELETE /rest/api/3/project/{projectIdOrKey}/role/{id}`

- Run by the tool [[jira_delete_actors_from_project_role]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/role/{{param:id}}?user={{param:user}}&group={{param:group}}&groupId={{param:groupId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project ID or project key (case sensitive).
- `id` (path, string, required) — The ID of the project role. Use Get all project roles to get a list of project role IDs.
- `user` (query, string, optional) — The user account ID of the user to remove from the project role.
- `group` (query, string, optional) — The name of the group to remove from the project role. This parameter cannot be used with the groupId parameter. As a group's name can change, use of groupId is recommended.
- `groupId` (query, string, optional) — The ID of the group to remove from the project role. This parameter cannot be used with the group parameter.

## Original description

Deletes actors from a project role for the project.

To remove default actors from the project role, use [Delete default actors from project role](#api-rest-api-3-role-id-actors-delete).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
