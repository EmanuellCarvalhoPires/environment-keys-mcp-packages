---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/objecttype
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: DELETE
path: "/objecttype/{id}"
category: "Objecttype"
writes_data: true
tool_note: "[[assets_delete_objecttype]]"
---
# Assets - DELETE objecttype {id}

**/objecttype/{id}** — `DELETE /objecttype/{id}`

- Run by the tool [[assets_delete_objecttype]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
DELETE https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/objecttype/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Delete an object type
