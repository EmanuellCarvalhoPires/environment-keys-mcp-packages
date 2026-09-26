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
path: "/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports"
category: "Pipelines"
writes_data: false
tool_note: "[[bitbucket_get_a_summary_of_test_reports_for_a_given_step_of_a_pi]]"
---
# Bitbucket - Get a summary of test reports for a given step of a pipeline

**Get a summary of test reports for a given step of a pipeline.** — `GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports`

- Run by the tool [[bitbucket_get_a_summary_of_test_reports_for_a_given_step_of_a_pi]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines/{{param:pipeline_uuid}}/steps/{{param:step_uuid}}/test_reports
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `pipeline_uuid` (path, string, required) — The UUID of the pipeline.
- `step_uuid` (path, string, required) — The UUID of the step.

