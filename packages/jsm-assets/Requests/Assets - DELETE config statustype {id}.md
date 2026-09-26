---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/config
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: DELETE
path: "/config/statustype/{id}"
category: "Config"
writes_data: true
tool_note: "[[assets_delete_config_statustype]]"
---
# Assets - DELETE config statustype {id}

**/config/statustype/{id}** — `DELETE /config/statustype/{id}`

- Run by the tool [[assets_delete_config_statustype]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
DELETE https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/config/statustype/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Delete an existing status
