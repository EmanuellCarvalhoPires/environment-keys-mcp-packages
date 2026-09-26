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
path: "/stakeholder-comms/cloudId/{cloudId}/api/stakeholders/from_similar_incidents/{incidentKey}"
category: "Stakeholder User management"
writes_data: false
---
# JSM Ops - Get stakeholders from similar incidents

**Get stakeholders from similar incidents** — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholders/from_similar_incidents/{incidentKey}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get stakeholders from similar incidents"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/stakeholders/from_similar_incidents/{{param:incidentKey}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `incidentKey` (path, string, required) — Key of the incident to find similar incidents for.

## Original description

Get stakeholders from incidents similar to the specified incident.
