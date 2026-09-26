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
path: "/stakeholder-comms/cloudId/{cloudId}/api/pages/draft/by_name/{name}"
category: "Status Page"
writes_data: false
---
# JSM Ops - Get draft page by name

**Get draft page by name** — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/draft/by_name/{name}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get draft page by name"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/pages/draft/by_name/{{param:name}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `name` (path, string, required) — Name of the draft page.

## Original description

Get a draft Status page by its name.
