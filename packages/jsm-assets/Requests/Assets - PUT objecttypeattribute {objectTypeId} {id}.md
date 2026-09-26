---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/objecttypeattribute
  - api/operation/update
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: PUT
path: "/objecttypeattribute/{objectTypeId}/{id}"
category: "Objecttypeattribute"
writes_data: true
tool_note: "[[assets_update_objecttypeattribute]]"
---
# Assets - PUT objecttypeattribute {objectTypeId} {id}

**/objecttypeattribute/{objectTypeId}/{id}** — `PUT /objecttypeattribute/{objectTypeId}/{id}`

- Run by the tool [[assets_update_objecttypeattribute]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
PUT https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/objecttypeattribute/{{param:objectTypeId}}/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `objectTypeId` (path, string, required) — Value of objectTypeId in the path.
- `id` (path, string, required) — Value of id in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "GPS coordinates of the office"
}
```

## Original description

Update an existing object type attribute
