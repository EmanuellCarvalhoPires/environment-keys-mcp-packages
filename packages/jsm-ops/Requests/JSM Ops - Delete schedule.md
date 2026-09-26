---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/schedules
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: DELETE
path: "/api/{cloudId}/v1/schedules/{id}"
category: "Schedules"
writes_data: true
---
# JSM Ops - Delete schedule

**Delete schedule** — `DELETE /api/{cloudId}/v1/schedules/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete schedule"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/schedules/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — ID of the schedule.

## Original description

Deletes the schedule with given id in the request.   **Permissions required:** Permission to delete the schedule: 
 - the user has delete configuration right. 
 - the user is the admin of the team that the schedule belongs to.
