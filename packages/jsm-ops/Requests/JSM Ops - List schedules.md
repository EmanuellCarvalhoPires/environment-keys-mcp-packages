---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/schedules
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/schedules"
category: "Schedules"
writes_data: false
---
# JSM Ops - List schedules

**List schedules** — `GET /api/{cloudId}/v1/schedules`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List schedules"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/schedules?query={{param:query}}&size={{param:size}}&offset={{param:offset}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `query` (query, string, optional) — The query keyword to filter schedules by name. It performs an exact match unless the keyword ends with a wildcard character , in which case it performs a prefix match. Matching is case-insensitive.
- `size` (query, string, optional) — The limit parameter controls the maximum number of items that may be returned for a single request.
- `offset` (query, string, optional) — The offset parameter controls the starting point within the collection of resource results.
- `expand` (query, string, optional) — The list of possible expansions in the response. Possible values: rotation.

## Original description

Lists all schedules that user can view. It optionally takes two parameters - offset and size.  **Permissions required:** Permission to access Jira Service Management; however, the list contains a schedule if: 
 - the user has read-only administrative right. 
 - the schedule's assigned team is one of the teams that the user belongs to. 
 - the user is added to a rotation of the schedule as a responder. 
 - a team is added to a rotation of the schedule as a responder, and the user is a member of this team. 
 - an escalation is added to a rotation of the schedule as a responder, and the user is a member of this escalation. 
 - there is an override to the user in the schedule.
