---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/action
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: POST
path: "/importsource/{importSourceId}/executions/{executionId}/history/failed"
category: "Importsource"
writes_data: true
tool_note: "[[assets_post_importsource_executions_history_failed]]"
---
# Assets - POST importsource {importSourceId} executions {executionId} history failed

**/importsource/{importSourceId}/executions/{executionId}/history/failed** — `POST /importsource/{importSourceId}/executions/{executionId}/history/failed`

- Run by the tool [[assets_post_importsource_executions_history_failed]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
POST https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/importsource/{{param:importSourceId}}/executions/{{param:executionId}}/history/failed
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `importSourceId` (path, string, required) — Value of importSourceId in the path.
- `executionId` (path, string, required) — Value of executionId in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "failureReason": "Connection timeout while fetching data from external source"
}
```

## Original description

Creates a failed import history record for the specified import source and execution with the given failure reason
