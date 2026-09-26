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
path: "/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}"
category: "Pipelines"
writes_data: false
tool_note: "[[bitbucket_get_a_pipeline]]"
---
# Bitbucket - Get a pipeline

**Get a pipeline** — `GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}`

- Run by the tool [[bitbucket_get_a_pipeline]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines/{{param:pipeline_uuid}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `pipeline_uuid` (path, string, required) — The pipeline UUID.

## Original description

Retrieve a specified pipeline
