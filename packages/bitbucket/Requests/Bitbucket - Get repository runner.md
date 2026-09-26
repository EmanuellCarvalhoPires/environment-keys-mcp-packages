---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/pipelines-config/runners/{runner_uuid}"
category: "Pipelines"
writes_data: false
tool_note: "[[bitbucket_get_repository_runner]]"
---
# Bitbucket - Get repository runner

**Get repository runner** — `GET /repositories/{workspace}/{repo_slug}/pipelines-config/runners/{runner_uuid}`

- Run by the tool [[bitbucket_get_repository_runner]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines-config/runners/{{param:runner_uuid}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `runner_uuid` (path, string, required) — The runner uuid.

## Original description

Retrieve repository runner by uuid.
