---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/objecttype
  - api/operation/action
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: POST
path: "/objecttype/{id}/position"
category: "Objecttype"
writes_data: true
tool_note: "[[assets_post_objecttype_position]]"
---
# Assets - POST objecttype {id} position

**/objecttype/{id}/position** — `POST /objecttype/{id}/position`

- Run by the tool [[assets_post_objecttype_position]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
POST https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/objecttype/{{param:id}}/position
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
  "toObjectTypeId": "2",
  "position": 0
}
```

## Original description

Change position of this object type
