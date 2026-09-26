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
path: "/importsource/{importSourceId}/executions/{importExecutionId}/data"
category: "Importsource"
writes_data: true
tool_note: "[[assets_post_importsource_executions_data]]"
---
# Assets - POST importsource {importSourceId} executions {importExecutionId} data

**/importsource/{importSourceId}/executions/{importExecutionId}/data** — `POST /importsource/{importSourceId}/executions/{importExecutionId}/data`

- Run by the tool [[assets_post_importsource_executions_data]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
POST https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/importsource/{{param:importSourceId}}/executions/{{param:importExecutionId}}/data
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
  "data": {
    "hardDrives": [
      {
        "id": "Hard drive ID",
        "label": "Hard drive label",
        "files": [
          {
            "path": "/file/path",
            "size": 123456
          }
        ]
      }
    ]
  },
  "clientGeneratedId": "a-unique-id",
  "completed": true
}
```

## Original description

Providing data to be ingested
