---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/schedule-overrides
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/schedules/{scheduleId}/overrides"
category: "Schedule overrides"
writes_data: false
---
# JSM Ops - List overrides

**List overrides** — `GET /api/{cloudId}/v1/schedules/{scheduleId}/overrides`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List overrides"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/schedules/{{param:scheduleId}}/overrides?size={{param:size}}&offset={{param:offset}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `scheduleId` (path, string, required) — ID of the schedule.
- `size` (query, string, optional) — The limit parameter controls the maximum number of items that may be returned for a single request.
- `offset` (query, string, optional) — The offset parameter controls the starting point within the collection of resource results.

## Original description

Lists all ongoing and future overrides of the schedule with given id in the request. It optionally takes two parameters - offset and size.  **Permissions required:** Permission to access to the schedule: 
 - the user has read-only administrative right. 
 - the schedule's assigned team is one of the teams that the user belongs to. 
 - the user is added to a rotation of the schedule as a responder. 
 - a team is added to a rotation of the schedule as a responder, and the user is a member of this team. 
 - an escalation is added to a rotation of the schedule as a responder, and the user is a member of this escalation. 
 - there is an override to the user in the schedule.
