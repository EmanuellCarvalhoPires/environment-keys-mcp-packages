---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/stakeholder-user-management
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/stakeholder-comms/cloudId/{cloudId}/api/stakeholders/by_assignment/v2"
category: "Stakeholder User management"
writes_data: false
---
# JSM Ops - Get stakeholders by assignment with pagination

**Get stakeholders by assignment with pagination** — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholders/by_assignment/v2`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get stakeholders by assignment with pagination"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/stakeholders/by_assignment/v2?assignmentId={{param:assignmentId}}&ari={{param:ari}}&assignmentType={{param:assignmentType}}&externalAssignmentId={{param:externalAssignmentId}}&first={{param:first}}&after={{param:after}}&last={{param:last}}&before={{param:before}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `assignmentId` (query, string, optional) — Assignment identifier.
- `ari` (query, string, optional) — Atlassian Resource Identifier of the assignment.
- `assignmentType` (query, string, optional) — Type of the assignment.
- `externalAssignmentId` (query, string, optional) — External system assignment identifier.
- `first` (query, string, optional) — Number of items to return from the start.
- `after` (query, string, optional) — Cursor for forward pagination.
- `last` (query, string, optional) — Number of items to return from the end.
- `before` (query, string, optional) — Cursor for backward pagination.

## Original description

Get a paginated list of stakholders by assignment.
