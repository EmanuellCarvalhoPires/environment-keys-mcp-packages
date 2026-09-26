---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: DELETE
path: "/repositories/{workspace}/{repo_slug}/pipelines-config/runners/{runner_uuid}"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_delete_repository_runner]]"
---
# Bitbucket - Delete repository runner

**Delete repository runner** — `DELETE /repositories/{workspace}/{repo_slug}/pipelines-config/runners/{runner_uuid}`

- Run by the tool [[bitbucket_delete_repository_runner]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines-config/runners/{{param:runner_uuid}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `runner_uuid` (path, string, required) — The runner uuid.

## Original description

Delete repository runner by uuid.
