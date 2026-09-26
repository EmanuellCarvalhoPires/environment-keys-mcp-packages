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
path: "/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}"
category: "Pipelines"
writes_data: false
tool_note: "[[bitbucket_get_a_step_of_a_pipeline]]"
---
# Bitbucket - Get a step of a pipeline

**Get a step of a pipeline** — `GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}`

- Run by the tool [[bitbucket_get_a_step_of_a_pipeline]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines/{{param:pipeline_uuid}}/steps/{{param:step_uuid}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `pipeline_uuid` (path, string, required) — The UUID of the pipeline.
- `step_uuid` (path, string, required) — The UUID of the step.

## Original description

Retrieve a given step of a pipeline.
