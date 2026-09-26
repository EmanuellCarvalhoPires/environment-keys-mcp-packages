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
path: "/repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}"
category: "Pipelines"
writes_data: false
tool_note: "[[bitbucket_get_a_schedule]]"
---
# Bitbucket - Get a schedule

**Get a schedule** — `GET /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}`

- Run by the tool [[bitbucket_get_a_schedule]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines_config/schedules/{{param:schedule_uuid}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `schedule_uuid` (path, string, required) — The uuid of the schedule.

## Original description

Retrieve a schedule by its UUID.
