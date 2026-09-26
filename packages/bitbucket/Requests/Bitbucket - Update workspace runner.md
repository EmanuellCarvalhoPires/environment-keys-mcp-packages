---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/workspaces/{workspace}/pipelines-config/runners/{runner_uuid}"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_update_workspace_runner]]"
---
# Bitbucket - Update workspace runner

**Update workspace runner** — `PUT /workspaces/{workspace}/pipelines-config/runners/{runner_uuid}`

- Run by the tool [[bitbucket_update_workspace_runner]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/workspaces/{{service.workspace}}/pipelines-config/runners/{{param:runner_uuid}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `runner_uuid` (path, string, required) — The runner uuid.

## Original description

Update workspace runner.
