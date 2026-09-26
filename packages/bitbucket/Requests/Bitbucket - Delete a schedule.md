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
path: "/repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_delete_a_schedule]]"
---
# Bitbucket - Delete a schedule

**Delete a schedule** — `DELETE /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}`

- Run by the tool [[bitbucket_delete_a_schedule]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines_config/schedules/{{param:schedule_uuid}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `schedule_uuid` (path, string, required) — The uuid of the schedule.

## Original description

Delete a schedule.
