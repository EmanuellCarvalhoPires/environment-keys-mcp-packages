---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: DELETE
path: "/importsource/{importSourceId}/importschedule/{importScheduleId}"
category: "Importsource"
writes_data: true
tool_note: "[[assets_delete_import_schedule]]"
---
# Assets - Delete import schedule

**Delete import schedule** — `DELETE /importsource/{importSourceId}/importschedule/{importScheduleId}`

- Run by the tool [[assets_delete_import_schedule]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
DELETE https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/importsource/{{param:importSourceId}}/importschedule/{{param:importScheduleId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `importSourceId` (path, string, required) — The ID of the import source
- `importScheduleId` (path, string, required) — The ID of the import schedule to delete

## Original description

Deletes a scheduled import configuration. The import source will remain, but will no longer execute on a schedule.
