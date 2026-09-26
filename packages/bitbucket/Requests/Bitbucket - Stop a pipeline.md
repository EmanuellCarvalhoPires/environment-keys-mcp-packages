---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/action
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/stopPipeline"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_stop_a_pipeline]]"
---
# Bitbucket - Stop a pipeline

**Stop a pipeline** — `POST /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/stopPipeline`

- Run by the tool [[bitbucket_stop_a_pipeline]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines/{{param:pipeline_uuid}}/stopPipeline
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `pipeline_uuid` (path, string, required) — The UUID of the pipeline.

## Original description

Signal the stop of a pipeline and all of its steps that not have completed yet.
