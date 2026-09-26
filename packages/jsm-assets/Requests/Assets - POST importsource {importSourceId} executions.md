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
path: "/importsource/{importSourceId}/executions"
category: "Importsource"
writes_data: true
tool_note: "[[assets_post_importsource_executions]]"
---
# Assets - POST importsource {importSourceId} executions

**/importsource/{importSourceId}/executions** — `POST /importsource/{importSourceId}/executions`

- Run by the tool [[assets_post_importsource_executions]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
POST https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/importsource/{{param:importSourceId}}/executions
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `importSourceId` (path, string, required) — Value of importSourceId in the path.

## Original description

Move to the data ingestion steps of external imports
