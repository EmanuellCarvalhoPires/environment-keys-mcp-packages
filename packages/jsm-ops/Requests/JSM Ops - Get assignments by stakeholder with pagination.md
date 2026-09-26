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
path: "/stakeholder-comms/cloudId/{cloudId}/api/assignments/by_stakeholder/v2"
category: "Stakeholder User management"
writes_data: false
---
# JSM Ops - Get assignments by stakeholder with pagination

**Get assignments by stakeholder with pagination** — `GET /stakeholder-comms/cloudId/{cloudId}/api/assignments/by_stakeholder/v2`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get assignments by stakeholder with pagination"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/assignments/by_stakeholder/v2?stakeholderId={{param:stakeholderId}}&ari={{param:ari}}&aaid={{param:aaid}}&emailId={{param:emailId}}&stakeholderGroupId={{param:stakeholderGroupId}}&atlassianTeamId={{param:atlassianTeamId}}&stakeholderType={{param:stakeholderType}}&first={{param:first}}&after={{param:after}}&last={{param:last}}&before={{param:before}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `stakeholderId` (query, string, optional) — Identifier of the stakeholder.
- `ari` (query, string, optional) — Atlassian Resource Identifier of the stakeholder.
- `aaid` (query, string, optional) — Atlassian Account ID of the stakeholder.
- `emailId` (query, string, optional) — Email address of the stakeholder.
- `stakeholderGroupId` (query, string, optional) — Stakeholder group identifier.
- `atlassianTeamId` (query, string, optional) — Atlassian team identifier.
- `stakeholderType` (query, string, optional) — Type of the stakeholder.
- `first` (query, string, optional) — Number of items to return from the start.
- `after` (query, string, optional) — Cursor for forward pagination.
- `last` (query, string, optional) — Number of items to return from the end.
- `before` (query, string, optional) — Cursor for backward pagination.

## Original description

Get assignments for a stakeholder with pagination support.
