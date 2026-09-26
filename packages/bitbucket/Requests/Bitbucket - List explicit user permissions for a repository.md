---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/permissions-config/users"
category: "Repositories"
writes_data: false
tool_note: "[[bitbucket_list_explicit_user_permissions_for_a_repository]]"
---
# Bitbucket - List explicit user permissions for a repository

**List explicit user permissions for a repository** — `GET /repositories/{workspace}/{repo_slug}/permissions-config/users`

- Run by the tool [[bitbucket_list_explicit_user_permissions_for_a_repository]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/permissions-config/users
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.

## Original description

Returns a paginated list of explicit user permissions for the given repository.
This endpoint does not support BBQL features.
