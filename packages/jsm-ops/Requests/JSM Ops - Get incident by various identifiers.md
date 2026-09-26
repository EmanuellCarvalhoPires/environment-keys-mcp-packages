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
path: "/stakeholder-comms/cloudId/{cloudId}/api/incidents/get"
category: "Status Page"
writes_data: false
---
# JSM Ops - Get incident by various identifiers

**Get incident by various identifiers** — `GET /stakeholder-comms/cloudId/{cloudId}/api/incidents/get`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get incident by various identifiers"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/incidents/get?incidentId={{param:incidentId}}&incidentCode={{param:incidentCode}}&externalIncidentId={{param:externalIncidentId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `incidentId` (query, string, optional) — Identifier of the incident.
- `incidentCode` (query, string, optional) — Incident code identifier.
- `externalIncidentId` (query, string, optional) — External system incident identifier.

## Original description

Get an incident by various identifiers such as incident ID, issue key, or other unique identifiers.
