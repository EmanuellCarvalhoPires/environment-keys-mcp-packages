---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/update
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: PUT
path: "/importsource/{importSourceId}/importschedule/{importScheduleId}"
category: "Importsource"
writes_data: true
tool_note: "[[assets_update_import_schedule]]"
---
# Assets - Update import schedule

**Update import schedule** — `PUT /importsource/{importSourceId}/importschedule/{importScheduleId}`

- Run by the tool [[assets_update_import_schedule]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
PUT https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/importsource/{{param:importSourceId}}/importschedule/{{param:importScheduleId}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `importSourceId` (path, string, required) — The ID of the import source
- `importScheduleId` (path, string, required) — The ID of the import schedule to update
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "startTime": "2024-02-01T10:00:00Z",
  "runInterval": "WEEKLY"
}
```

## Original description

Updates an existing scheduled import configuration. You can modify the start time, run interval, or callback URL.
