---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/import
  - api/operation/action
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: POST
path: "/import/start/{id}"
category: "Import"
writes_data: true
tool_note: "[[assets_post_import_start]]"
---
# Assets - POST import start {id}

**/import/start/{id}** — `POST /import/start/{id}`

- Run by the tool [[assets_post_import_start]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
POST https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/import/start/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Start configured imports. To see an ongoing import see the Progress resource
