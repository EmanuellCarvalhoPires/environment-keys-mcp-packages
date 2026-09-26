---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/get
  - api/effect/read
up: "[[MCP - Assets]]"
app: "Assets"
method: GET
path: "/importsource/{importSourceId}/mapping/progress/{resourceId}"
category: "Importsource"
writes_data: false
tool_note: "[[assets_get_importsource_mapping_progress]]"
---
# Assets - GET importsource {importSourceId} mapping progress {resourceId}

**/importsource/{importSourceId}/mapping/progress/{resourceId}** — `GET /importsource/{importSourceId}/mapping/progress/{resourceId}`

- Run by the tool [[assets_get_importsource_mapping_progress]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/importsource/{{param:importSourceId}}/mapping/progress/{{param:resourceId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `importSourceId` (path, string, required) — Value of importSourceId in the path.
- `resourceId` (path, string, required) — Value of resourceId in the path.

## Original description

Get the progress of an asynchronous schema and mapping operation
