---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/repositories/{workspace}/{repo_slug}/pipelines-config/runners"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_create_repository_runner]]"
---
# Bitbucket - Create repository runner

**Create repository runner** — `POST /repositories/{workspace}/{repo_slug}/pipelines-config/runners`

- Run by the tool [[bitbucket_create_repository_runner]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines-config/runners
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository.

## Original description

Create repository runner.
