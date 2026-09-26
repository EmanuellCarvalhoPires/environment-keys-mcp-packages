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
path: "/stakeholder-comms/cloudId/{cloudId}/api/incidents/templates/{incidentTemplateId}"
category: "Status Page"
writes_data: false
---
# JSM Ops - Get incident template

**Get incident template** — `GET /stakeholder-comms/cloudId/{cloudId}/api/incidents/templates/{incidentTemplateId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get incident template"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/incidents/templates/{{param:incidentTemplateId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `incidentTemplateId` (path, string, required) — Identifier of the incident template.

## Original description

Get an incident template by its ID.
