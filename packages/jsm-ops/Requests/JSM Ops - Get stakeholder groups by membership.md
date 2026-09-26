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
path: "/stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/by_membership/{id}"
category: "Stakeholder User management"
writes_data: false
---
# JSM Ops - Get stakeholder groups by membership

**Get stakeholder groups by membership** — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/by_membership/{id}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get stakeholder groups by membership"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/stakeholder_groups/by_membership/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Identifier of the stakeholder.

## Original description

Get stakeholder groups that a stakeholder belongs to.
