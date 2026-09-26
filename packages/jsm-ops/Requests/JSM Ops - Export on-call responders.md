---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/schedule-on-calls
  - api/operation/list
  - api/effect/read
  - api/format/binary
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/schedules/on-calls/{userIdentifier}.ics"
category: "Schedule on-calls"
writes_data: false
---
# JSM Ops - Export on-call responders

**Export on-call responders** — `GET /api/{cloudId}/v1/schedules/on-calls/{userIdentifier}.ics`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Export on-call responders"`.
- **Format:** the response is binary (file/image); the plugin returns the body as text.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/schedules/on-calls/{{param:userIdentifier}}.ics
Authorization: {{service.auth_token}}
Accept: text/calendar
```

## Parameters

- `userIdentifier` (path, string, required) — ID of the user whose on-call calendar to be exported.

## Original description

Exports the on-call periods in the calendar (.ics) format for the user with given id in the request.
 
 **Permissions required:** Permission to export to the user on-calls: 
 - the user exports the on-call calendar for themselves. 
 - the user exports the on-call calendar for another user, and the requesting user is the admin. 
 - the user exports the on-call calendar for another user, and the requesting user is the team admin in one of the teams of the requested user.
