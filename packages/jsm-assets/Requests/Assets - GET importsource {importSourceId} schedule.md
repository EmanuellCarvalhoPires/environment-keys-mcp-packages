---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
app: "Assets"
method: GET
path: "/importsource/{importSourceId}/schedule"
category: "Importsource"
writes_data: false
tool_note: "[[assets_get_importsource_schedule]]"
---
# Assets - GET importsource {importSourceId} schedule

**/importsource/{importSourceId}/schedule** — `GET /importsource/{importSourceId}/schedule`

- Run by the tool [[assets_get_importsource_schedule]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/importsource/{{param:importSourceId}}/schedule
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `importSourceId` (path, string, required) — Value of importSourceId in the path.

## Original description

Retrieve links for import schedule operations (create, get, update, delete). Returns a createSchedule link to POST a new schedule, and if a schedule already exists, returns a schedule link that can be used with GET, PUT, or DELETE operations.
