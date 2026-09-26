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
path: "/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/logs/{log_uuid}"
category: "Pipelines"
writes_data: false
tool_note: "[[bitbucket_get_the_logs_for_the_build_container_or_a_service_cont]]"
---
# Bitbucket - Get the logs for the build container or a service container for a given step of a pipeline

**Get the logs for the build container or a service container for a given step of a pipeline.** — `GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/logs/{log_uuid}`

- Run by the tool [[bitbucket_get_the_logs_for_the_build_container_or_a_service_cont]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines/{{param:pipeline_uuid}}/steps/{{param:step_uuid}}/logs/{{param:log_uuid}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `pipeline_uuid` (path, string, required) — The UUID of the pipeline.
- `step_uuid` (path, string, required) — The UUID of the step.
- `log_uuid` (path, string, required) — For the main build container specify the step UUID; for a service container specify the service container UUID

## Original description

Retrieve the log file for a build container or service container.

This endpoint supports (and encourages!) the use of [HTTP Range requests](https://tools.ietf.org/html/rfc7233) to deal with potentially very large log files.
