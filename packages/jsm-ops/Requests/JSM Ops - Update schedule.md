---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/schedules
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: PATCH
path: "/api/{cloudId}/v1/schedules/{id}"
category: "Schedules"
writes_data: true
---
# JSM Ops - Update schedule

**Update schedule** — `PATCH /api/{cloudId}/v1/schedules/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Update schedule"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
PATCH https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/schedules/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates the schedule with given id in the request.   **Permissions required:** Permission to update the schedule: 
 - the user has edit configuration right. 
 - the user is the admin of the team that the schedule belongs to.
