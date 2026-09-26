---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: POST
path: "/repositories/{workspace}/{repo_slug}/pipelines_config/schedules"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_create_a_schedule]]"
---
# Bitbucket - Create a schedule

**Create a schedule** — `POST /repositories/{workspace}/{repo_slug}/pipelines_config/schedules`

- Run by the tool [[bitbucket_create_a_schedule]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pipelines_config/schedules
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Create a schedule for the given repository.
