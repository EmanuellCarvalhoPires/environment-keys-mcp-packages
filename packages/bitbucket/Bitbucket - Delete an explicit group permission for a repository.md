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
path: "/repositories/{workspace}/{repo_slug}/permissions-config/groups/{group_slug}"
category: "Repositories"
writes_data: true
tool_note: "[[bitbucket_delete_an_explicit_group_permission_for_a_repository]]"
---
# Bitbucket - Delete an explicit group permission for a repository

**Delete an explicit group permission for a repository** — `DELETE /repositories/{workspace}/{repo_slug}/permissions-config/groups/{group_slug}`

- Run by the tool [[bitbucket_delete_an_explicit_group_permission_for_a_repository]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/permissions-config/groups/{{param:group_slug}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `group_slug` (path, string, required) — Value of groupslug in the path.

## Original description

Deletes the repository group permission between the requested repository and group, if one exists.

Only users with admin permission for the repository may access this resource.

The only authentication method supported for this endpoint is via app passwords.
