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
path: "/repositories/{workspace}/{repo_slug}/pipelines_config/schedules"
category: "Pipelines"
writes_data: false
tool_note: "[[bitbucket_list_schedules]]"
---
# Bitbucket - List schedules

**List schedules** — `GET /repositories/{workspace}/{repo_slug}/pipelines_config/schedules`

- Run by the tool [[bitbucket_list_schedules]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines_config/schedules
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `repo_slug` (path, string, required) — The repository.

## Original description

Retrieve the configured schedules for the given repository.
