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
path: "/workspaces/{workspace}/pipelines-config/runners"
category: "Pipelines"
writes_data: false
tool_note: "[[bitbucket_get_workspace_runners]]"
---
# Bitbucket - Get workspace runners

**Get workspace runners** — `GET /workspaces/{workspace}/pipelines-config/runners`

- Run by the tool [[bitbucket_get_workspace_runners]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/workspaces/{{service.workspace}}/pipelines-config/runners
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Retrieve workspace runners.
