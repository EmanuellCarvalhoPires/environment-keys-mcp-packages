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
path: "/importsource/{importSourceId}/configstatus"
category: "Importsource"
writes_data: false
tool_note: "[[assets_get_importsource_configstatus]]"
---
# Assets - GET importsource {importSourceId} configstatus

**/importsource/{importSourceId}/configstatus** — `GET /importsource/{importSourceId}/configstatus`

- Run by the tool [[assets_get_importsource_configstatus]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/importsource/{{param:importSourceId}}/configstatus
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `importSourceId` (path, string, required) — Value of importSourceId in the path.

## Original description

Get the current status of the import configuration
