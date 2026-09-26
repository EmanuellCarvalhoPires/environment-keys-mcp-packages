---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/workspaces/{workspace}/projects/{project_key}/permissions-config/users/{selected_user_id}"
category: "Projects"
writes_data: true
tool_note: "[[bitbucket_update_an_explicit_user_permission_for_a_project]]"
---
# Bitbucket - Update an explicit user permission for a project

**Update an explicit user permission for a project** — `PUT /workspaces/{workspace}/projects/{project_key}/permissions-config/users/{selected_user_id}`

- Run by the tool [[bitbucket_update_an_explicit_user_permission_for_a_project]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/workspaces/{{service.workspace}}/projects/{{param:project_key}}/permissions-config/users/{{param:selected_user_id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `project_key` (path, string, required) — Value of projectkey in the path.
- `selected_user_id` (path, string, required) — Value of selecteduserid in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates the explicit user permission for a given user and project. The selected
user must be a member of the workspace, and cannot be the workspace owner.

Only users with admin permission for the project may access this resource.

Due to security concerns, the JWT and OAuth authentication methods are unsupported.
This is to ensure integrations and add-ons are not allowed to change permissions.

Permissions can be:

* `admin`
* `create-repo`
* `write`
* `read`
