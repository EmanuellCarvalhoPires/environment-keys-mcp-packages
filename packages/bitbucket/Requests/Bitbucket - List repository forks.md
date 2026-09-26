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
path: "/repositories/{workspace}/{repo_slug}/forks"
category: "Repositories"
writes_data: false
tool_note: "[[bitbucket_list_repository_forks]]"
---
# Bitbucket - List repository forks

**List repository forks** — `GET /repositories/{workspace}/{repo_slug}/forks`

- Run by the tool [[bitbucket_list_repository_forks]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/forks?role={{param:role}}&q={{param:q}}&sort={{param:sort}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `role` (query, string, optional) — Filters the result based on the authenticated user's role on each repository. member: returns repositories to which the user has explicit read access contributor: returns repositories to which the use…
- `q` (query, string, optional) — Query string to narrow down the response as per filtering and sorting.
- `sort` (query, string, optional) — Field by which the results should be sorted as per filtering and sorting.

## Original description

Returns a paginated list of all the forks of the specified
repository.
