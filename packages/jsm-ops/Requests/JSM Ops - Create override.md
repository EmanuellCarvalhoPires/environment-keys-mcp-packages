---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/schedule-overrides
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/schedules/{scheduleId}/overrides"
category: "Schedule overrides"
writes_data: true
---
# JSM Ops - Create override

**Create override** — `POST /api/{cloudId}/v1/schedules/{scheduleId}/overrides`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Create override"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/schedules/{{param:scheduleId}}/overrides
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `scheduleId` (path, string, required) — ID of the schedule.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a new override for the schedule with given id and properties.  **Permissions required:** Permission to create an override: 
 - the user has edit configuration right. 
 - the user is a member of the team that the schedule belongs to. 
 - the user is adding override to themself. 
 - the user exists in the schedule directly or indirectly.
