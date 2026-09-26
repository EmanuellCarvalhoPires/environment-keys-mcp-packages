---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/branching-model
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/effective-branching-model"
category: "Branching model"
writes_data: false
tool_note: "[[bitbucket_get_the_effective_or_currently_applied_branching_model]]"
---
# Bitbucket - Get the effective, or currently applied, branching model for a repository

**Get the effective, or currently applied, branching model for a repository** — `GET /repositories/{workspace}/{repo_slug}/effective-branching-model`

- Run by the tool [[bitbucket_get_the_effective_or_currently_applied_branching_model]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/effective-branching-model
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.

