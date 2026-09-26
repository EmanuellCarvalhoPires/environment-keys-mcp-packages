---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/schedule-rotations
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/schedules/{scheduleId}/rotations"
category: "Schedule rotations"
writes_data: true
---
# JSM Ops - Create rotation

**Create rotation** — `POST /api/{cloudId}/v1/schedules/{scheduleId}/rotations`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Create rotation"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/schedules/{{param:scheduleId}}/rotations
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `scheduleId` (path, string, required) — ID of the schedule.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a new rotation for the schedule with given id and properties.  **Permissions required:** Permission to edit a schedule: 
 - the user has edit configuration right. 
 - the user is the admin of the team that the schedule belongs to.
