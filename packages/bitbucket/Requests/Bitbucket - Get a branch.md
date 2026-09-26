---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/refs
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/refs/branches/{name}"
category: "Refs"
writes_data: false
tool_note: "[[bitbucket_get_a_branch]]"
---
# Bitbucket - Get a branch

**Get a branch** — `GET /repositories/{workspace}/{repo_slug}/refs/branches/{name}`

- Run by the tool [[bitbucket_get_a_branch]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/refs/branches/{{param:name}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `name` (path, string, required) — Value of name in the path.

## Original description

Returns a branch object within the specified repository.

This call requires authentication. Private repositories require the
caller to authenticate with an account that has appropriate
authorization.

For Git, the branch name should not include any prefixes (e.g.
refs/heads).
