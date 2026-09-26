---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/object
  - api/operation/create
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: POST
path: "/object/create"
category: "Object"
writes_data: true
tool_note: "[[assets_post_object_create]]"
---
# Assets - POST object create

**/object/create** — `POST /object/create`

- Run by the tool [[assets_post_object_create]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
POST https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/object/create
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "objectTypeId": "23",
  "attributes": [
    {
      "objectTypeAttributeId": "135",
      "objectAttributeValues": [
        {
          "value": "NY-1"
        }
      ]
    },
    {
      "objectTypeAttributeId": "144",
      "objectAttributeValues": [
        {
          "value": "99"
        }
      ]
    }
  ]
}
```

## Original description

Create a new object in Assets
