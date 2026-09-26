---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: DELETE
path: "/workspaces/{workspace}/projects/{project_key}/permissions-config/groups/{group_slug}"
category: "Projects"
writes_data: true
tool_note: "[[bitbucket_delete_an_explicit_group_permission_for_a_project]]"
---
# Bitbucket - Delete an explicit group permission for a project

**Delete an explicit group permission for a project** — `DELETE /workspaces/{workspace}/projects/{project_key}/permissions-config/groups/{group_slug}`

- Run by the tool [[bitbucket_delete_an_explicit_group_permission_for_a_project]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/workspaces/{{service.workspace}}/projects/{{param:project_key}}/permissions-config/groups/{{param:group_slug}}
Authorization: {{service.auth_token}}
```

## Parameters

- `project_key` (path, string, required) — Value of projectkey in the path.
- `group_slug` (path, string, required) — Value of groupslug in the path.

## Original description

Deletes the project group permission between the requested project and group, if one exists.

Only users with admin permission for the project may access this resource.
