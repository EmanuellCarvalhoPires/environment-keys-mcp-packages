---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/get
  - api/effect/read
up: "[[MCP - Assets]]"
app: "Assets"
method: GET
path: "/importsource/{id}"
category: "Importsource"
writes_data: false
tool_note: "[[assets_get_import_source_by_id]]"
---
# Assets - Get import source by ID

**Get import source by ID** — `GET /importsource/{id}`

- Run by the tool [[assets_get_import_source_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/importsource/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Retrieves a specific import source configuration by its ID. If scheduled imports are enabled, the response includes scheduling information.
