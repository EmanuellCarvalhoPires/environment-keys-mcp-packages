---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/schedule-rotations
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: DELETE
path: "/api/{cloudId}/v1/schedules/{scheduleId}/rotations/{id}"
category: "Schedule rotations"
writes_data: true
---
# JSM Ops - Delete rotation

**Delete rotation** — `DELETE /api/{cloudId}/v1/schedules/{scheduleId}/rotations/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete rotation"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/schedules/{{param:scheduleId}}/rotations/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `scheduleId` (path, string, required) — ID of the schedule.
- `id` (path, string, required) — ID of the rotation.

## Original description

Deletes the rotation of a schedule with given IDs in the request.   **Permissions required:** Permission to delete the rotation: 
 - the user has delete configuration right. 
 - the user is the admin of the team that rotation's schedule belongs to.
