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
path: "/repositories/{workspace}/{repo_slug}"
category: "Repositories"
writes_data: false
tool_note: "[[bitbucket_get_a_repository]]"
---
# Bitbucket - Get a repository

**Get a repository** — `GET /repositories/{workspace}/{repo_slug}`

- Run by the tool [[bitbucket_get_a_repository]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.

## Original description

Returns the object describing this repository.
