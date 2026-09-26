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
path: "/workspaces/{workspace}/projects/{project_key}/permissions-config/users/{selected_user_id}"
category: "Projects"
writes_data: true
tool_note: "[[bitbucket_delete_an_explicit_user_permission_for_a_project]]"
---
# Bitbucket - Delete an explicit user permission for a project

**Delete an explicit user permission for a project** — `DELETE /workspaces/{workspace}/projects/{project_key}/permissions-config/users/{selected_user_id}`

- Run by the tool [[bitbucket_delete_an_explicit_user_permission_for_a_project]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/workspaces/{{service.workspace}}/projects/{{param:project_key}}/permissions-config/users/{{param:selected_user_id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `project_key` (path, string, required) — Value of projectkey in the path.
- `selected_user_id` (path, string, required) — Value of selecteduserid in the path.

## Original description

Deletes the project user permission between the requested project and user, if one exists.

Only users with admin permission for the project may access this resource.

Due to security concerns, the JWT and OAuth authentication methods are unsupported.
This is to ensure integrations and add-ons are not allowed to change permissions.
