---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/repositories/{workspace}/{repo_slug}/permissions-config/groups/{group_slug}"
category: "Repositories"
writes_data: true
tool_note: "[[bitbucket_update_an_explicit_group_permission_for_a_repository]]"
---
# Bitbucket - Update an explicit group permission for a repository

**Update an explicit group permission for a repository** — `PUT /repositories/{workspace}/{repo_slug}/permissions-config/groups/{group_slug}`

- Run by the tool [[bitbucket_update_an_explicit_group_permission_for_a_repository]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/permissions-config/groups/{{param:group_slug}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `group_slug` (path, string, required) — Value of groupslug in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates the group permission, or grants a new permission if one does not already exist.

Only users with admin permission for the repository may access this resource.

The only authentication method supported for this endpoint is via app passwords.

Permissions can be:

* `admin`
* `write`
* `read`
