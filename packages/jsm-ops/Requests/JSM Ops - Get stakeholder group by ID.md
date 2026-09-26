---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/stakeholder-user-management
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/{groupId}"
category: "Stakeholder User management"
writes_data: false
---
# JSM Ops - Get stakeholder group by ID

**Get stakeholder group by ID** — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/{groupId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get stakeholder group by ID"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/stakeholder_groups/{{param:groupId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `groupId` (path, string, required) — Identifier of the stakeholder group.

## Original description

Get a stakeholder group by its ID for stakeholder communications.
