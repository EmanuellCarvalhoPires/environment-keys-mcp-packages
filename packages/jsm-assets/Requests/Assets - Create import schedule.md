---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/create
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: POST
path: "/importsource/{importSourceId}/importschedule"
category: "Importsource"
writes_data: true
tool_note: "[[assets_create_import_schedule]]"
---
# Assets - Create import schedule

**Create import schedule** — `POST /importsource/{importSourceId}/importschedule`

- Run by the tool [[assets_create_import_schedule]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
POST https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/importsource/{{param:importSourceId}}/importschedule
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `importSourceId` (path, string, required) — The ID of the import source to schedule
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "startTime": "2024-01-15T02:00:00Z",
  "runInterval": "DAILY"
}
```

## Original description

Creates a new scheduled import configuration for the specified import source. Scheduled imports allow you to automate data imports on a recurring basis (daily, weekly, monthly) or run them once at a specific time.
