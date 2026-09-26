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
path: "/stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/components/uptime"
category: "Status Page"
writes_data: false
---
# JSM Ops - Get components uptime for page

**Get components uptime for page** — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/components/uptime`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get components uptime for page"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/pages/{{param:pageId}}/components/uptime?startDate={{param:startDate}}&endDate={{param:endDate}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `pageId` (path, string, required) — Identifier of the page.
- `startDate` (query, string, optional) — Start of the period.
- `endDate` (query, string, optional) — End of the period.

## Original description

Get uptime information for components associated with a Status page over a given period.
