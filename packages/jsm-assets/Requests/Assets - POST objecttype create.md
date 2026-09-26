---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/objecttype
  - api/operation/create
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: POST
path: "/objecttype/create"
category: "Objecttype"
writes_data: true
tool_note: "[[assets_post_objecttype_create]]"
---
# Assets - POST objecttype create

**/objecttype/create** — `POST /objecttype/create`

- Run by the tool [[assets_post_objecttype_create]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
POST https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/objecttype/create
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "inherited": false,
  "abstractObjectType": false,
  "objectSchemaId": "6",
  "iconId": "13",
  "name": "Office",
  "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin nec ex."
}
```

## Original description

Create a new object type
