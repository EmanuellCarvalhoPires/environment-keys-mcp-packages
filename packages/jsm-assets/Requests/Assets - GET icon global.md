---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/icon
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
app: "Assets"
method: GET
path: "/icon/global"
category: "Icon"
writes_data: false
tool_note: "[[assets_get_icon_global]]"
---
# Assets - GET icon global

**/icon/global** — `GET /icon/global`

- Run by the tool [[assets_get_icon_global]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/icon/global
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Return all global icons i.e. icons not associated with a particular object schema
