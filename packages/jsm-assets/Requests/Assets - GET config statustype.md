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
path: "/config/statustype"
category: "Config"
writes_data: false
tool_note: "[[assets_get_config_statustype]]"
---
# Assets - GET config statustype

**/config/statustype** — `GET /config/statustype`

- Run by the tool [[assets_get_config_statustype]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/config/statustype?objectSchemaId={{param:objectSchemaId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `objectSchemaId` (query, string, optional) — Include statuses for the object schema id. If supplied statuses for the object schema will be returned otherwise all global will be returned

## Original description

Find all status
