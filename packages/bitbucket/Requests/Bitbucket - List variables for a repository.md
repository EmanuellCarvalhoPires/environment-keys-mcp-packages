---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/pipelines_config/variables"
category: "Pipelines"
writes_data: false
tool_note: "[[bitbucket_list_variables_for_a_repository]]"
---
# Bitbucket - List variables for a repository

**List variables for a repository** — `GET /repositories/{workspace}/{repo_slug}/pipelines_config/variables`

- Run by the tool [[bitbucket_list_variables_for_a_repository]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines_config/variables
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository.

## Original description

Find repository level variables.
