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
path: "/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports/test_cases/{test_case_uuid}/test_case_reasons"
category: "Pipelines"
writes_data: false
tool_note: "[[bitbucket_get_test_case_reasons_output_for_a_given_test_case_in]]"
---
# Bitbucket - Get test case reasons (output) for a given test case in a step of a pipeline

**Get test case reasons (output) for a given test case in a step of a pipeline.** — `GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports/test_cases/{test_case_uuid}/test_case_reasons`

- Run by the tool [[bitbucket_get_test_case_reasons_output_for_a_given_test_case_in]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines/{{param:pipeline_uuid}}/steps/{{param:step_uuid}}/test_reports/test_cases/{{param:test_case_uuid}}/test_case_reasons
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `pipeline_uuid` (path, string, required) — The UUID of the pipeline.
- `step_uuid` (path, string, required) — The UUID of the step.
- `test_case_uuid` (path, string, required) — The UUID of the test case.

