---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/workspaces/{workspace}/permissions/repositories/{repo_slug}"
category: "Workspaces"
writes_data: false
tool_note: "[[bitbucket_list_a_repository_permissions_for_a_workspace]]"
---
# Bitbucket - List a repository permissions for a workspace

**List a repository permissions for a workspace** — `GET /workspaces/{workspace}/permissions/repositories/{repo_slug}`

- Run by the tool [[bitbucket_list_a_repository_permissions_for_a_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/permissions/repositories/{{param:repo_slug}}?q={{param:q}}&sort={{param:sort}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `q` (query, string, optional) — Query string to narrow down the response as per filtering and sorting.
- `sort` (query, string, optional) — Name of a response property sort the result by as per filtering and sorting.

## Original description

Returns an object for the repository permission of each user in the
requested repository.

Permissions returned are effective permissions: the highest level of
permission the user has. This does not distinguish between direct and
indirect (group) privileges.

Only users with admin permission for the repository may access this resource.

Permissions can be:

* `admin`
* `write`
* `read`

Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering)
by user, or permission by adding the following query string parameters:

* `q=permission>"read"`
* `sort=user.display_name`

Note that the query parameter values need to be URL escaped so that `=`
would become `%3D`.
