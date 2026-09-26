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
path: "/workspaces/{workspace}/pipelines-config/runners"
category: "Pipelines"
writes_data: true
tool_note: "[[bitbucket_create_workspace_runner]]"
---
# Bitbucket - Create workspace runner

**Create workspace runner** — `POST /workspaces/{workspace}/pipelines-config/runners`

- Run by the tool [[bitbucket_create_workspace_runner]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
POST {{service.url}}/workspaces/{{service.workspace}}/pipelines-config/runners
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Create workspace runner.
