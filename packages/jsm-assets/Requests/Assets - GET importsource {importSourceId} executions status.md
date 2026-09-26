---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
app: "Assets"
method: GET
path: "/importsource/{importSourceId}/executions/status"
category: "Importsource"
writes_data: false
tool_note: "[[assets_get_importsource_executions_status_get]]"
---
# Assets - GET importsource {importSourceId} executions status

**/importsource/{importSourceId}/executions/status** — `GET /importsource/{importSourceId}/executions/status`

- Run by the tool [[assets_get_importsource_executions_status_get]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/importsource/{{param:importSourceId}}/executions/status
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `importSourceId` (path, string, required) — Value of importSourceId in the path.

## Original description

Get the status of the most recently created import execution
