---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/workspaces/{workspace}/projects/{project_key}/permissions-config/users/{selected_user_id}"
category: "Projects"
writes_data: false
tool_note: "[[bitbucket_get_an_explicit_user_permission_for_a_project]]"
---
# Bitbucket - Get an explicit user permission for a project

**Get an explicit user permission for a project** — `GET /workspaces/{workspace}/projects/{project_key}/permissions-config/users/{selected_user_id}`

- Run by the tool [[bitbucket_get_an_explicit_user_permission_for_a_project]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/projects/{{param:project_key}}/permissions-config/users/{{param:selected_user_id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `project_key` (path, string, required) — Value of projectkey in the path.
- `selected_user_id` (path, string, required) — Value of selecteduserid in the path.

## Original description

Returns the explicit user permission for a given user and project.

Only users with admin permission for the project may access this resource.

Permissions can be:

* `admin`
* `create-repo`
* `write`
* `read`
* `none`
