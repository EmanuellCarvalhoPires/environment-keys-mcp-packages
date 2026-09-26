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
path: "/workspaces/{workspace}/projects/{project_key}/permissions-config/groups/{group_slug}"
category: "Projects"
writes_data: false
tool_note: "[[bitbucket_get_an_explicit_group_permission_for_a_project]]"
---
# Bitbucket - Get an explicit group permission for a project

**Get an explicit group permission for a project** — `GET /workspaces/{workspace}/projects/{project_key}/permissions-config/groups/{group_slug}`

- Run by the tool [[bitbucket_get_an_explicit_group_permission_for_a_project]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/projects/{{param:project_key}}/permissions-config/groups/{{param:group_slug}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `project_key` (path, string, required) — Value of projectkey in the path.
- `group_slug` (path, string, required) — Value of groupslug in the path.

## Original description

Returns the group permission for a given group and project.

Only users with admin permission for the project may access this resource.

Permissions can be:

* `admin`
* `create-repo`
* `write`
* `read`
* `none`
