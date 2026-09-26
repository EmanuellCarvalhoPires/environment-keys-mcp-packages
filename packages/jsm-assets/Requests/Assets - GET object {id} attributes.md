---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/object
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
app: "Assets"
method: GET
path: "/object/{id}/attributes"
category: "Object"
writes_data: false
tool_note: "[[assets_get_object_attributes]]"
---
# Assets - GET object {id} attributes

**/object/{id}/attributes** — `GET /object/{id}/attributes`

- Run by the tool [[assets_get_object_attributes]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/object/{{param:id}}/attributes
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

List all attributes for the given object
