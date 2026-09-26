---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/schedules
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/schedules"
category: "Schedules"
writes_data: true
---
# JSM Ops - Create schedule

**Create schedule** — `POST /api/{cloudId}/v1/schedules`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Create schedule"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/schedules
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a schedule with given properties.  **Permissions required:** Permission to create a schedule: 
 - the user has edit configuration right. 
 - the user is the admin of the team that the schedule belongs to.
