---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/schedule-overrides
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/schedules/{scheduleId}/overrides/{alias}"
category: "Schedule overrides"
writes_data: false
---
# JSM Ops - Get override

**Get override** — `GET /api/{cloudId}/v1/schedules/{scheduleId}/overrides/{alias}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get override"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/schedules/{{param:scheduleId}}/overrides/{{param:alias}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `scheduleId` (path, string, required) — ID of the schedule.
- `alias` (path, string, required) — Alias of the override.

## Original description

Returns the details of the override of a schedule with given IDs in the request.   **Permissions required:** Permission to access to the schedule: 
 - the user has read-only administrative right. 
 - the schedule's assigned team is one of the teams that the user belongs to. 
 - the user is added to a rotation of the schedule as a responder. 
 - a team is added to a rotation of the schedule as a responder, and the user is a member of this team. 
 - an escalation is added to a rotation of the schedule as a responder, and the user is a member of this escalation. 
 - there is an override to the user in the schedule.
