---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/schedule-timelines
  - api/operation/list
  - api/effect/read
  - api/format/binary
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/schedules/{scheduleId}.ics"
category: "Schedule timelines"
writes_data: false
---
# JSM Ops - Export schedule timeline

**Export schedule timeline** — `GET /api/{cloudId}/v1/schedules/{scheduleId}.ics`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Export schedule timeline"`.
- **Format:** the response is binary (file/image); the plugin returns the body as text.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/schedules/{{param:scheduleId}}.ics
Authorization: {{service.auth_token}}
Accept: text/calendar
```

## Parameters

- `scheduleId` (path, string, required) — ID of the schedule.

## Original description

Exports the timeline in the calendar (.ics) format for the schedule with given id in the request. The time range of the export starts from the beginning of the current month and ends one year after the start date.  **Permissions required:** Permission to access to the schedule: 
 - the user has read-only administrative right. 
 - the schedule's assigned team is one of the teams that the user belongs to. 
 - the user is added to a rotation of the schedule as a responder. 
 - a team is added to a rotation of the schedule as a responder, and the user is a member of this team. 
 - an escalation is added to a rotation of the schedule as a responder, and the user is a member of this escalation. 
 - there is an override to the user in the schedule.
