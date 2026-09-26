---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/schedule-rotations
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/schedules/{scheduleId}/rotations"
category: "Schedule rotations"
writes_data: false
---
# JSM Ops - List rotations

**List rotations** — `GET /api/{cloudId}/v1/schedules/{scheduleId}/rotations`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List rotations"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/schedules/{{param:scheduleId}}/rotations?size={{param:size}}&offset={{param:offset}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `scheduleId` (path, string, required) — ID of the schedule.
- `size` (query, string, optional) — The limit parameter controls the maximum number of items that may be returned for a single request.
- `offset` (query, string, optional) — The offset parameter controls the starting point within the collection of resource results.

## Original description

Lists all rotations of the schedule with given id in the request. It optionally takes two parameters - offset and size.  **Permissions required:** Permission to access to the schedule: 
 - the user has read-only administrative right. 
 - the schedule's assigned team is one of the teams that the user belongs to. 
 - the user is added to a rotation of the schedule as a responder. 
 - a team is added to a rotation of the schedule as a responder, and the user is a member of this team. 
 - an escalation is added to a rotation of the schedule as a responder, and the user is a member of this escalation. 
 - there is an override to the user in the schedule.
