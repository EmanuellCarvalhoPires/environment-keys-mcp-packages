---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/objecttypeattribute
  - api/operation/action
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: POST
path: "/objecttypeattribute/{objectTypeId}"
category: "Objecttypeattribute"
writes_data: true
tool_note: "[[assets_post_objecttypeattribute]]"
---
# Assets - POST objecttypeattribute {objectTypeId}

**/objecttypeattribute/{objectTypeId}** — `POST /objecttypeattribute/{objectTypeId}`

- Run by the tool [[assets_post_objecttypeattribute]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
POST https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/objecttypeattribute/{{param:objectTypeId}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `objectTypeId` (path, string, required) — Value of objectTypeId in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "name": "Geolocation",
  "type": "0",
  "defaultTypeId": "0"
}
```

## Original description

Create a new attribute on the given object type
