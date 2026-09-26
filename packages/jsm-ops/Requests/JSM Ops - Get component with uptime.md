---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/status-page
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/stakeholder-comms/cloudId/{cloudId}/api/components/{componentId}/uptime"
category: "Status Page"
writes_data: false
---
# JSM Ops - Get component with uptime

**Get component with uptime** — `GET /stakeholder-comms/cloudId/{cloudId}/api/components/{componentId}/uptime`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get component with uptime"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/components/{{param:componentId}}/uptime?startDate={{param:startDate}}&endDate={{param:endDate}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `componentId` (path, string, required) — Identifier of the component.
- `startDate` (query, string, optional) — Start of the period.
- `endDate` (query, string, optional) — End of the period.

## Original description

Get a component with its uptime information by component ID.
