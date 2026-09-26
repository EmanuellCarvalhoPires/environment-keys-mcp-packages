---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/objecttypeattribute
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: DELETE
path: "/objecttypeattribute/{id}"
category: "Objecttypeattribute"
writes_data: true
tool_note: "[[assets_delete_objecttypeattribute]]"
---
# Assets - DELETE objecttypeattribute {id}

**/objecttypeattribute/{id}** — `DELETE /objecttypeattribute/{id}`

- Run by the tool [[assets_delete_objecttypeattribute]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
DELETE https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/objecttypeattribute/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Delete an existing object type attribute
