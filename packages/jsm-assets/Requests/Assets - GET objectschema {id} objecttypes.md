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
path: "/objectschema/{id}/objecttypes"
category: "Objectschema"
writes_data: false
tool_note: "[[assets_get_objectschema_objecttypes]]"
---
# Assets - GET objectschema {id} objecttypes

**/objectschema/{id}/objecttypes** — `GET /objectschema/{id}/objecttypes`

- Run by the tool [[assets_get_objectschema_objecttypes]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/objectschema/{{param:id}}/objecttypes
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Find all object types for this object schema
