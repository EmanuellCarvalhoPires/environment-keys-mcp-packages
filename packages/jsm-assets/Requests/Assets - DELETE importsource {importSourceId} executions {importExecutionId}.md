---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: DELETE
path: "/importsource/{importSourceId}/executions/{importExecutionId}"
category: "Importsource"
writes_data: true
tool_note: "[[assets_delete_importsource_executions]]"
---
# Assets - DELETE importsource {importSourceId} executions {importExecutionId}

**/importsource/{importSourceId}/executions/{importExecutionId}** — `DELETE /importsource/{importSourceId}/executions/{importExecutionId}`

- Run by the tool [[assets_delete_importsource_executions]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
DELETE https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/importsource/{{param:importSourceId}}/executions/{{param:importExecutionId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `importSourceId` (path, string, required) — Value of importSourceId in the path.
- `importExecutionId` (path, string, required) — Value of importExecutionId in the path.

## Original description

Cancel current on-going import
