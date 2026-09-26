---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/icon
  - api/operation/get
  - api/effect/read
up: "[[MCP - Assets]]"
app: "Assets"
method: GET
path: "/icon/{id}"
category: "Icon"
writes_data: false
tool_note: "[[assets_get_icon]]"
---
# Assets - GET icon {id}

**/icon/{id}** — `GET /icon/{id}`

- Run by the tool [[assets_get_icon]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/icon/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Load a single icon by id
