---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/config
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
app: "Assets"
method: GET
path: "/config/referencetype"
category: "Config"
writes_data: false
tool_note: "[[assets_get_config_referencetype]]"
---
# Assets - GET config referencetype

**/config/referencetype** — `GET /config/referencetype`

- Run by the tool [[assets_get_config_referencetype]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/config/referencetype?objectSchemaId={{param:objectSchemaId}}&includeAll={{param:includeAll}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `objectSchemaId` (query, string, optional) — Include reference types for the object schema id. If supplied reference types for the object schema will be returned otherwise all global will be returned
- `includeAll` (query, string, optional) — Include all reference types. Defaults to false

## Original description

Get reference type
