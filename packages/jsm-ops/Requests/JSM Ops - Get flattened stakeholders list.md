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
path: "/stakeholder-comms/cloudId/{cloudId}/api/stakeholders/flattened_list"
category: "Stakeholder User management"
writes_data: false
---
# JSM Ops - Get flattened stakeholders list

**Get flattened stakeholders list** — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholders/flattened_list`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get flattened stakeholders list"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/stakeholders/flattened_list?groupIds={{param:groupIds}}&teamIds={{param:teamIds}}&externalUserContextToken={{param:externalUserContextToken}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `groupIds` (query, string, optional) — Filter by stakeholder group IDs.
- `teamIds` (query, string, optional) — Filter by team IDs.
- `externalUserContextToken` (query, string, optional) — External user context token.

## Original description

Get a detailed list of stakeholders including those from groups
