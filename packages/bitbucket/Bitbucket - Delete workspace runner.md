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
path: "/workspaces/{workspace}/pipelines-config/runners/{runner_uuid}"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_delete_workspace_runner]]"
---
# Bitbucket - Delete workspace runner

**Delete workspace runner** — `DELETE /workspaces/{workspace}/pipelines-config/runners/{runner_uuid}`

- Run by the tool [[bitbucket_delete_workspace_runner]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
DELETE {{service.url}}/workspaces/{{service.workspace}}/pipelines-config/runners/{{param:runner_uuid}}
Authorization: {{service.auth_token}}
```

## Parameters

- `runner_uuid` (path, string, required) — The runner uuid.

## Original description

Delete workspace runner by uuid.
