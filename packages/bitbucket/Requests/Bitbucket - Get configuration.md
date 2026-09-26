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
path: "/repositories/{workspace}/{repo_slug}/pipelines_config"
category: "Pipelines"
writes_data: false
tool_note: "[[bitbucket_get_configuration]]"
---
# Bitbucket - Get configuration

**Get configuration** — `GET /repositories/{workspace}/{repo_slug}/pipelines_config`

- Run by the tool [[bitbucket_get_configuration]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines_config
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository.

## Original description

Retrieve the repository pipelines configuration.
