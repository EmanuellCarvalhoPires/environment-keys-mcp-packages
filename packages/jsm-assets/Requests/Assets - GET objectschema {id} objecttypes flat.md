---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/objectschema
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
app: "Assets"
method: GET
path: "/objectschema/{id}/objecttypes/flat"
category: "Objectschema"
writes_data: false
tool_note: "[[assets_get_objectschema_objecttypes_flat]]"
---
# Assets - GET objectschema {id} objecttypes flat

**/objectschema/{id}/objecttypes/flat** — `GET /objectschema/{id}/objecttypes/flat`

- Run by the tool [[assets_get_objectschema_objecttypes_flat]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/objectschema/{{param:id}}/objecttypes/flat
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Find all object types for this object schema
