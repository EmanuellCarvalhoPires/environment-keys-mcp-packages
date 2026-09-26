---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/config
  - api/operation/get
  - api/effect/read
up: "[[MCP - Assets]]"
app: "Assets"
method: GET
path: "/config/statustype/{id}"
category: "Config"
writes_data: false
tool_note: "[[assets_get_config_statustype_get]]"
---
# Assets - GET config statustype {id}

**/config/statustype/{id}** — `GET /config/statustype/{id}`

- Run by the tool [[assets_get_config_statustype_get]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/config/statustype/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Find a status by id
