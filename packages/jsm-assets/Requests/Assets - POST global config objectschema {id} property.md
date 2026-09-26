---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/global
  - api/operation/action
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: POST
path: "/global/config/objectschema/{id}/property"
category: "Global"
writes_data: true
tool_note: "[[assets_post_global_config_objectschema_property]]"
---
# Assets - POST global config objectschema {id} property

**/global/config/objectschema/{id}/property** — `POST /global/config/objectschema/{id}/property`

- Run by the tool [[assets_post_global_config_objectschema_property]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
POST https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/global/config/objectschema/{{param:id}}/property
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Object schema id
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "allowOtherObjectSchema": true,
  "validateQuickCreate": true,
  "quickCreateObjects": true
}
```

## Original description

Update general configuration for object schema
