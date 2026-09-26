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
path: "/importsource/{importSourceId}/executions/{importExecutionId}/status"
category: "Importsource"
writes_data: false
tool_note: "[[assets_get_importsource_executions_status]]"
---
# Assets - GET importsource {importSourceId} executions {importExecutionId} status

**/importsource/{importSourceId}/executions/{importExecutionId}/status** — `GET /importsource/{importSourceId}/executions/{importExecutionId}/status`

- Run by the tool [[assets_get_importsource_executions_status]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/importsource/{{param:importSourceId}}/executions/{{param:importExecutionId}}/status
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `importSourceId` (path, string, required) — Value of importSourceId in the path.
- `importExecutionId` (path, string, required) — Value of importExecutionId in the path.

## Original description

Get the status of the import
