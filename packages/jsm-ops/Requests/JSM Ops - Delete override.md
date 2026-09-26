---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/schedule-overrides
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: DELETE
path: "/api/{cloudId}/v1/schedules/{scheduleId}/overrides/{alias}"
category: "Schedule overrides"
writes_data: true
---
# JSM Ops - Delete override

**Delete override** — `DELETE /api/{cloudId}/v1/schedules/{scheduleId}/overrides/{alias}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete override"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/schedules/{{param:scheduleId}}/overrides/{{param:alias}}
Authorization: {{service.auth_token}}
```

## Parameters

- `scheduleId` (path, string, required) — ID of the schedule.
- `alias` (path, string, required) — Alias of the override.

## Original description

Deletes the override of a schedule with given IDs in the request.   **Permissions required:** Permission to delete the override: 
 - the user is the responder of the override. 
 - the user has edit configuration right. 
 - the user is the admin of the team that the schedule belongs to.
