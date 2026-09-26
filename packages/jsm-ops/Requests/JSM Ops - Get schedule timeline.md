---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/schedule-timelines
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/schedules/{scheduleId}/timeline"
category: "Schedule timelines"
writes_data: false
---
# JSM Ops - Get schedule timeline

**Get schedule timeline** — `GET /api/{cloudId}/v1/schedules/{scheduleId}/timeline`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get schedule timeline"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/schedules/{{param:scheduleId}}/timeline?interval={{param:interval}}&intervalUnit={{param:intervalUnit}}&date={{param:date}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `scheduleId` (path, string, required) — ID of the schedule.
- `interval` (query, string, optional) — The length of the timeline calculation time range as an integer in intervalUnits.
- `intervalUnit` (query, string, optional) — The unit of the timeline calculation time range.
- `date` (query, string, optional) — The date to calculate timeline according to. The interval, intervalUnit, and this field are combined to calculate to time range of the timeline.
- `expand` (query, string, optional) — The list of possible expansions in the response. The default response only contains the timeline of the final layer.

## Original description

Returns the timeline of the schedule with given id in the request. The time range of the timeline can go back at most one year from today and as far as two years from today. Therefore, query parameters should be given accordingly.  **Permissions required:** Permission to access to the schedule: 
 - the user has read-only administrative right. 
 - the schedule's assigned team is one of the teams that the user belongs to. 
 - the user is added to a rotation of the schedule as a responder. 
 - a team is added to a rotation of the schedule as a responder, and the user is a member of this team. 
 - an escalation is added to a rotation of the schedule as a responder, and the user is a member of this escalation. 
 - there is an override to the user in the schedule.
