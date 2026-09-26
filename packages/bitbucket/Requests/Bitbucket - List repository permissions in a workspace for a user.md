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
path: "/user/workspaces/{workspace}/permissions/repositories"
category: "Repositories"
writes_data: false
tool_note: "[[bitbucket_list_repository_permissions_in_a_workspace_for_a_user]]"
---
# Bitbucket - List repository permissions in a workspace for a user

**List repository permissions in a workspace for a user** — `GET /user/workspaces/{workspace}/permissions/repositories`

- Run by the tool [[bitbucket_list_repository_permissions_in_a_workspace_for_a_user]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/user/workspaces/{{service.workspace}}/permissions/repositories?q={{param:q}}&sort={{param:sort}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `q` (query, string, optional) — Query string to narrow down the response as per filtering and sorting.
- `sort` (query, string, optional) — Name of a response property sort the result by as per filtering and sorting.

## Original description

Returns an object for each repository the caller has explicit access to in the
specified workspace and their effective permission — the highest level of
permission the caller has. This does not return public repositories that the
user was not granted any specific permission in, and does not distinguish between
explicit and implicit privileges.

Permissions can be:

* `admin`
* `write`
* `read`

Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by
repository or permission by adding the following query string
parameters:

* `q=repository.name="bits"` or `q=permission>"read"`
* `sort=repository.name`

Note that the query parameter values need to be URL escaped so that `=`
would become `%3D`.
