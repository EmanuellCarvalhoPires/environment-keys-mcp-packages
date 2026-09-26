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
path: "/stakeholder-comms/cloudId/{cloudId}/api/incidents/templates/list"
category: "Status Page"
writes_data: false
---
# JSM Ops - List incident templates

**List incident templates** — `GET /stakeholder-comms/cloudId/{cloudId}/api/incidents/templates/list`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List incident templates"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/incidents/templates/list?pageId={{param:pageId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `pageId` (query, string, optional) — Identifier of the page to filter templates.

## Original description

List incident templates used for stakeholder communciations.
