---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/repositories/{workspace}/{repo_slug}/pipelines-config/runners/{runner_uuid}"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_update_repository_runner]]"
---
# Bitbucket - Update repository runner

**Update repository runner** — `PUT /repositories/{workspace}/{repo_slug}/pipelines-config/runners/{runner_uuid}`

- Run by the tool [[bitbucket_update_repository_runner]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines-config/runners/{{param:runner_uuid}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `runner_uuid` (path, string, required) — The runner uuid.

## Original description

Update repository runner.
