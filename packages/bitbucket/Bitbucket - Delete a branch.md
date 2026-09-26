---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/refs
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: DELETE
path: "/repositories/{workspace}/{repo_slug}/refs/branches/{name}"
category: "Refs"
writes_data: true
tool_note: "[[bitbucket_delete_a_branch]]"
---
# Bitbucket - Delete a branch

**Delete a branch** — `DELETE /repositories/{workspace}/{repo_slug}/refs/branches/{name}`

- Run by the tool [[bitbucket_delete_a_branch]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/refs/branches/{{param:name}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `name` (path, string, required) — Value of name in the path.

## Original description

Delete a branch in the specified repository.

The main branch is not allowed to be deleted and will return a 400
response.

The branch name should not include any prefixes (e.g.
refs/heads).
