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
path: "/stakeholder-comms/cloudId/{cloudId}/api/stakeholders/by_ari"
category: "Stakeholder User management"
writes_data: false
---
# JSM Ops - Get stakeholders by ARI list

**Get stakeholders by ARI list** — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholders/by_ari`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get stakeholders by ARI list"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/stakeholders/by_ari?stakeholderAris={{param:stakeholderAris}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `stakeholderAris` (query, string, required) — List of Atlassian Resource Identifiers.

## Original description

Get stakeholders by a list of Atlassian Resource Identifiers (ARIs).
