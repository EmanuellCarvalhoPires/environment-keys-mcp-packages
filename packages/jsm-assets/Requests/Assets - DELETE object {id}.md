---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/object
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: DELETE
path: "/object/{id}"
category: "Object"
writes_data: true
tool_note: "[[assets_delete_object]]"
---
# Assets - DELETE object {id}

**/object/{id}** — `DELETE /object/{id}`

- Run by the tool [[assets_delete_object]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
DELETE https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/object/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Delete the referenced object
