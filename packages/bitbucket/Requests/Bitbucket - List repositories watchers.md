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
path: "/repositories/{workspace}/{repo_slug}/watchers"
category: "Repositories"
writes_data: false
tool_note: "[[bitbucket_list_repositories_watchers]]"
---
# Bitbucket - List repositories watchers

**List repositories watchers** — `GET /repositories/{workspace}/{repo_slug}/watchers`

- Run by the tool [[bitbucket_list_repositories_watchers]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/watchers
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.

## Original description

Returns a paginated list of all the watchers on the specified
repository.
