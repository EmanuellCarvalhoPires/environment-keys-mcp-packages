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
path: "/workspaces/{workspace}/projects/{project_key}/permissions-config/groups/{group_slug}"
category: "Projects"
writes_data: true
tool_note: "[[bitbucket_update_an_explicit_group_permission_for_a_project]]"
---
# Bitbucket - Update an explicit group permission for a project

**Update an explicit group permission for a project** — `PUT /workspaces/{workspace}/projects/{project_key}/permissions-config/groups/{group_slug}`

- Run by the tool [[bitbucket_update_an_explicit_group_permission_for_a_project]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/workspaces/{{service.workspace}}/projects/{{param:project_key}}/permissions-config/groups/{{param:group_slug}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `project_key` (path, string, required) — Value of projectkey in the path.
- `group_slug` (path, string, required) — Value of groupslug in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates the group permission, or grants a new permission if one does not already exist.

Only users with admin permission for the project may access this resource.

Due to security concerns, the JWT and OAuth authentication methods are unsupported.
This is to ensure integrations and add-ons are not allowed to change permissions.

Permissions can be:

* `admin`
* `create-repo`
* `write`
* `read`
