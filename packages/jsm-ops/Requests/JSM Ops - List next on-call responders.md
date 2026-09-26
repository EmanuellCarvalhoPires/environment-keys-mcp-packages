---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/schedule-on-calls
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/schedules/{scheduleId}/next-on-calls"
category: "Schedule on-calls"
writes_data: false
---
# JSM Ops - List next on-call responders

**List next on-call responders** — `GET /api/{cloudId}/v1/schedules/{scheduleId}/next-on-calls`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List next on-call responders"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/schedules/{{param:scheduleId}}/next-on-calls?flat={{param:flat}}&date={{param:date}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `scheduleId` (path, string, required) — ID of the schedule.
- `flat` (query, string, optional) — When enabled, returns only the user names of all next on-call participants in user type. Otherwise, returns the complete flattening tree for next on-calls.
- `date` (query, string, optional) — The date for which the schedule's next on-calls are requested.

## Original description

Lists the next on-call responders at a specific time for the schedule with given id in the request.  **Permissions required:** Permission to access to the schedule: 
 - the user has read-only administrative right. 
 - the schedule's assigned team is one of the teams that the user belongs to. 
 - the user is added to a rotation of the schedule as a responder. 
 - a team is added to a rotation of the schedule as a responder, and the user is a member of this team. 
 - an escalation is added to a rotation of the schedule as a responder, and the user is a member of this escalation. 
 - there is an override to the user in the schedule.
