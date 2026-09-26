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
path: "/repositories/{workspace}/{repo_slug}/hooks/{uid}"
category: "Repositories"
writes_data: true
tool_note: "[[bitbucket_delete_a_webhook_for_a_repository]]"
---
# Bitbucket - Delete a webhook for a repository

**Delete a webhook for a repository** — `DELETE /repositories/{workspace}/{repo_slug}/hooks/{uid}`

- Run by the tool [[bitbucket_delete_a_webhook_for_a_repository]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/hooks/{{param:uid}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `uid` (path, string, required) — Value of uid in the path.

## Original description

Deletes the specified webhook subscription from the given
repository.
