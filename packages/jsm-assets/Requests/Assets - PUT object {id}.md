---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/object
  - api/operation/update
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: PUT
path: "/object/{id}"
category: "Object"
writes_data: true
tool_note: "[[assets_update_object]]"
---
# Assets - PUT object {id}

**/object/{id}** — `PUT /object/{id}`

- Run by the tool [[assets_update_object]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
PUT https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/object/{{param:id}}
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
  "attributes": [
    {
      "objectTypeAttributeId": "265",
      "objectAttributeValues": [
        {
          "value": "A placeholder value"
        }
      ]
    }
  ],
  "objectTypeId": "23",
  "avatarUUID": "",
  "hasAvatar": false
}
```

## Original description

Update an existing object in Assets
