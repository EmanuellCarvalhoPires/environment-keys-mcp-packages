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
path: "/workspaces/{workspace}/pipelines-config/runners/{runner_uuid}"
category: "Pipelines"
writes_data: false
tool_note: "[[bitbucket_get_workspace_runner]]"
---
# Bitbucket - Get workspace runner

**Get workspace runner** — `GET /workspaces/{workspace}/pipelines-config/runners/{runner_uuid}`

- Run by the tool [[bitbucket_get_workspace_runner]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/pipelines-config/runners/{{param:runner_uuid}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `runner_uuid` (path, string, required) — The runner uuid.

## Original description

Get workspace runner by uuid.
