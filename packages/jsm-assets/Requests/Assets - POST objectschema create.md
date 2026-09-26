---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/objectschema
  - api/operation/create
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: POST
path: "/objectschema/create"
category: "Objectschema"
writes_data: true
tool_note: "[[assets_post_objectschema_create]]"
---
# Assets - POST objectschema create

**/objectschema/create** — `POST /objectschema/create`

- Run by the tool [[assets_post_objectschema_create]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
POST https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/objectschema/create
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "name": "Computers",
  "objectSchemaKey": "COMP",
  "description": "The IT department schema"
}
```

## Original description

Create a new object schema
