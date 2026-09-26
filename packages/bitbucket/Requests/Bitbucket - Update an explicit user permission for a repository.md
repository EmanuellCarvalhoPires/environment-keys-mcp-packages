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
path: "/repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id}"
category: "Repositories"
writes_data: true
tool_note: "[[bitbucket_update_an_explicit_user_permission_for_a_repository]]"
---
# Bitbucket - Update an explicit user permission for a repository

**Update an explicit user permission for a repository** — `PUT /repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id}`

- Run by the tool [[bitbucket_update_an_explicit_user_permission_for_a_repository]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/permissions-config/users/{{param:selected_user_id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `selected_user_id` (path, string, required) — Value of selecteduserid in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates the explicit user permission for a given user and repository. The selected user must be a member of
the workspace, and cannot be the workspace owner.
Only users with admin permission for the repository may access this resource.

The only authentication method for this endpoint is via app passwords.

Permissions can be:

* `admin`
* `write`
* `read`
