---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/workspaces/{workspace}/projects/{project_key}/permissions-config/users"
category: "Projects"
writes_data: false
tool_note: "[[bitbucket_list_explicit_user_permissions_for_a_project]]"
---
# Bitbucket - List explicit user permissions for a project

**List explicit user permissions for a project** — `GET /workspaces/{workspace}/projects/{project_key}/permissions-config/users`

- Run by the tool [[bitbucket_list_explicit_user_permissions_for_a_project]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/projects/{{param:project_key}}/permissions-config/users
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `project_key` (path, string, required) — Value of projectkey in the path.

## Original description

Returns a paginated list of explicit user permissions for the given project.
This endpoint does not support BBQL features.
