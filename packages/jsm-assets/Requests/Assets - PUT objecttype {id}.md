---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/objecttype
  - api/operation/update
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: PUT
path: "/objecttype/{id}"
category: "Objecttype"
writes_data: true
tool_note: "[[assets_update_objecttype]]"
---
# Assets - PUT objecttype {id}

**/objecttype/{id}** — `PUT /objecttype/{id}`

- Run by the tool [[assets_update_objecttype]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
PUT https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/objecttype/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update an existing object type
