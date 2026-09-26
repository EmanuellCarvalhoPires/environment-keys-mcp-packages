---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/objectschema
  - api/operation/update
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: PUT
path: "/objectschema/{id}"
category: "Objectschema"
writes_data: true
tool_note: "[[assets_update_objectschema]]"
---
# Assets - PUT objectschema {id}

**/objectschema/{id}** — `PUT /objectschema/{id}`

- Run by the tool [[assets_update_objectschema]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
PUT https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/objectschema/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
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

Update an object schema
