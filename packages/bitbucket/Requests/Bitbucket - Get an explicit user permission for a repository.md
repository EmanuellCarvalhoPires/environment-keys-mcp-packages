---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id}"
category: "Repositories"
writes_data: false
tool_note: "[[bitbucket_get_an_explicit_user_permission_for_a_repository]]"
---
# Bitbucket - Get an explicit user permission for a repository

**Get an explicit user permission for a repository** — `GET /repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id}`

- Run by the tool [[bitbucket_get_an_explicit_user_permission_for_a_repository]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/permissions-config/users/{{param:selected_user_id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `selected_user_id` (path, string, required) — Value of selecteduserid in the path.

## Original description

Returns the explicit user permission for a given user and repository.

Only users with admin permission for the repository may access this resource.

Permissions can be:

* `admin`
* `write`
* `read`
* `none`
