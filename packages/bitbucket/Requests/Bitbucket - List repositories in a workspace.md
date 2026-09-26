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
path: "/repositories/{workspace}"
category: "Repositories"
writes_data: false
tool_note: "[[bitbucket_list_repositories_in_a_workspace]]"
---
# Bitbucket - List repositories in a workspace

**List repositories in a workspace** — `GET /repositories/{workspace}`

- Run by the tool [[bitbucket_list_repositories_in_a_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}?role={{param:role}}&q={{param:q}}&sort={{param:sort}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `role` (query, string, optional) — Filters the result based on the authenticated user's role on each repository. member: returns repositories to which the user has explicit read access contributor: returns repositories to which the use…
- `q` (query, string, optional) — Query string to narrow down the response as per filtering and sorting.
- `sort` (query, string, optional) — Field by which the results should be sorted as per filtering and sorting.

## Original description

Returns a paginated list of all repositories owned by the specified
workspace.

The result can be narrowed down based on the authenticated user's role.

E.g. with `?role=contributor`, only those repositories that the
authenticated user has write access to are returned (this includes any
repo the user is an admin on, as that implies write access).

This endpoint also supports filtering and sorting of the results. See
[filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.
