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
path: "/importsource/{importSourceId}/schema-and-mapping"
category: "Importsource"
writes_data: false
tool_note: "[[assets_get_importsource_schema_and_mapping]]"
---
# Assets - GET importsource {importSourceId} schema-and-mapping

**/importsource/{importSourceId}/schema-and-mapping** — `GET /importsource/{importSourceId}/schema-and-mapping`

- Run by the tool [[assets_get_importsource_schema_and_mapping]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/importsource/{{param:importSourceId}}/schema-and-mapping
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `importSourceId` (path, string, required) — Value of importSourceId in the path.

## Original description

Get the current schema and mapping of the import configuration
