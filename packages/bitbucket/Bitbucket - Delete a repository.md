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
path: "/repositories/{workspace}/{repo_slug}"
category: "Repositories"
writes_data: true
tool_note: "[[bitbucket_delete_a_repository]]"
---
# Bitbucket - Delete a repository

**Delete a repository** — `DELETE /repositories/{workspace}/{repo_slug}`

- Run by the tool [[bitbucket_delete_a_repository]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}?redirect_to={{param:redirect_to}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `redirect_to` (query, string, optional) — If a repository has been moved to a new location, use this parameter to show users a friendly message in the Bitbucket UI that the repository has moved to a new location.

## Original description

Deletes the repository. This is an irreversible operation.

This does not affect its forks.
