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
path: "/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps"
category: "Pipelines"
writes_data: false
tool_note: "[[bitbucket_list_steps_for_a_pipeline]]"
---
# Bitbucket - List steps for a pipeline

**List steps for a pipeline** — `GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps`

- Run by the tool [[bitbucket_list_steps_for_a_pipeline]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines/{{param:pipeline_uuid}}/steps
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `pipeline_uuid` (path, string, required) — The UUID of the pipeline.

## Original description

Find steps for the given pipeline.
