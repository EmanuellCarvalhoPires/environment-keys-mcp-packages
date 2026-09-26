---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/schedule-overrides
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: PUT
path: "/api/{cloudId}/v1/schedules/{scheduleId}/overrides/{alias}"
category: "Schedule overrides"
writes_data: true
---
# JSM Ops - Update override

**Update override** — `PUT /api/{cloudId}/v1/schedules/{scheduleId}/overrides/{alias}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Update override"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
PUT https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/schedules/{{param:scheduleId}}/overrides/{{param:alias}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `scheduleId` (path, string, required) — ID of the schedule.
- `alias` (path, string, required) — Alias of the override.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates the override of a schedule with given IDs in the request.  **Permissions required:** Permission to update an override: 
 - the user has edit configuration right. 
 - the user is a member of the team that the schedule belongs to. 
 - the user is adding override to themself. 
 - the user exists in the schedule directly or indirectly by flattening.
