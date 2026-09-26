---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: DELETE
path: "/repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id}"
category: "Repositories"
writes_data: true
tool_note: "[[bitbucket_delete_an_explicit_user_permission_for_a_repository]]"
---
# Bitbucket - Delete an explicit user permission for a repository

**Delete an explicit user permission for a repository** — `DELETE /repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id}`

- Run by the tool [[bitbucket_delete_an_explicit_user_permission_for_a_repository]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/permissions-config/users/{{param:selected_user_id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `selected_user_id` (path, string, required) — Value of selecteduserid in the path.

## Original description

Deletes the repository user permission between the requested repository and user, if one exists.

Only users with admin permission for the repository may access this resource.

The only authentication method for this endpoint is via app passwords.
