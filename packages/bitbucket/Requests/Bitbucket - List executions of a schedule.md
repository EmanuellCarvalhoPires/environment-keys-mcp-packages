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
path: "/repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}/executions"
category: "Pipelines"
writes_data: false
tool_note: "[[bitbucket_list_executions_of_a_schedule]]"
---
# Bitbucket - List executions of a schedule

**List executions of a schedule** — `GET /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}/executions`

- Run by the tool [[bitbucket_list_executions_of_a_schedule]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines_config/schedules/{{param:schedule_uuid}}/executions
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `schedule_uuid` (path, string, required) — The uuid of the schedule.

## Original description

Retrieve the executions of a given schedule.
