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
path: "/importsource/{importSourceId}/importschedule/{importScheduleId}"
category: "Importsource"
writes_data: false
tool_note: "[[assets_get_import_schedule]]"
---
# Assets - Get import schedule

**Get import schedule** — `GET /importsource/{importSourceId}/importschedule/{importScheduleId}`

- Run by the tool [[assets_get_import_schedule]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/importsource/{{param:importSourceId}}/importschedule/{{param:importScheduleId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `importSourceId` (path, string, required) — The ID of the import source
- `importScheduleId` (path, string, required) — The ID of the import schedule

## Original description

Retrieves a specific scheduled import configuration by ID
