---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/progress
  - api/operation/get
  - api/effect/read
up: "[[MCP - Assets]]"
app: "Assets"
method: GET
path: "/progress/category/imports/{id}"
category: "Progress"
writes_data: false
tool_note: "[[assets_get_progress_category_imports]]"
---
# Assets - GET progress category imports {id}

**/progress/category/imports/{id}** — `GET /progress/category/imports/{id}`

- Run by the tool [[assets_get_progress_category_imports]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/progress/category/imports/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Show ongoing import process
