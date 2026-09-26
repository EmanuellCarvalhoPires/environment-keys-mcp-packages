---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/status-page
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/stakeholder-comms/cloudId/{cloudId}/api/pages/subdomain/suggest/{pageName}"
category: "Status Page"
writes_data: false
---
# JSM Ops - Get unique subdomain suggestion

**Get unique subdomain suggestion** — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/subdomain/suggest/{pageName}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get unique subdomain suggestion"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/pages/subdomain/suggest/{{param:pageName}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `pageName` (path, string, required) — Name of the page to generate subdomain suggestion for.

## Original description

Get a unique subdomain suggestion for a Status page based on the page name.
