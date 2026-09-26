---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/update
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: PUT
path: "/importsource/{importSourceId}/executions/{importExecutionId}/progress"
category: "Importsource"
writes_data: true
tool_note: "[[assets_update_importsource_executions_progress]]"
---
# Assets - PUT importsource {importSourceId} executions {importExecutionId} progress

**/importsource/{importSourceId}/executions/{importExecutionId}/progress** — `PUT /importsource/{importSourceId}/executions/{importExecutionId}/progress`

- Run by the tool [[assets_update_importsource_executions_progress]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
PUT https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/importsource/{{param:importSourceId}}/executions/{{param:importExecutionId}}/progress
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `importSourceId` (path, string, required) — Value of importSourceId in the path.
- `importExecutionId` (path, string, required) — Value of importExecutionId in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "steps": {
    "total": 3,
    "current": 2,
    "description": "Gathering data"
  },
  "objects": {
    "total": 500,
    "processed": 125
  }
}
```

## Original description

Submit progress of ingesting data
