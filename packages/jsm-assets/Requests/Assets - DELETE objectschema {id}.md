---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/objectschema
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: DELETE
path: "/objectschema/{id}"
category: "Objectschema"
writes_data: true
tool_note: "[[assets_delete_objectschema]]"
---
# Assets - DELETE objectschema {id}

**/objectschema/{id}** — `DELETE /objectschema/{id}`

- Run by the tool [[assets_delete_objectschema]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
DELETE https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/objectschema/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Delete a schema
