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
path: "/stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/{groupId}/memberships"
category: "Stakeholder User management"
writes_data: false
---
# JSM Ops - Get memberships by group ID

**Get memberships by group ID** — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/{groupId}/memberships`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get memberships by group ID"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/stakeholder_groups/{{param:groupId}}/memberships?cursor={{param:cursor}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `groupId` (path, string, required) — Identifier of the stakeholder group.
- `cursor` (query, string, optional) — Cursor for pagination.
- `limit` (query, string, optional) — Maximum number of memberships to return.

## Original description

Get all members for a stakeholder group.
