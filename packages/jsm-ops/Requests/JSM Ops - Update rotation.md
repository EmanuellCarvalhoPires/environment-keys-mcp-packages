---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/schedule-rotations
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: PATCH
path: "/api/{cloudId}/v1/schedules/{scheduleId}/rotations/{id}"
category: "Schedule rotations"
writes_data: true
---
# JSM Ops - Update rotation

**Update rotation** — `PATCH /api/{cloudId}/v1/schedules/{scheduleId}/rotations/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Update rotation"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
PATCH https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/schedules/{{param:scheduleId}}/rotations/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `scheduleId` (path, string, required) — ID of the schedule.
- `id` (path, string, required) — ID of the rotation.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates the rotation of a schedule with given IDs in the request.   **Permissions required:** Permission to edit a schedule: 
 - the user has edit configuration right. 
 - the user is the admin of the team that the schedule belongs to.
