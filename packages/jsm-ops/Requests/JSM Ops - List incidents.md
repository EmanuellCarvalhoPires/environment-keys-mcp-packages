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
path: "/stakeholder-comms/cloudId/{cloudId}/api/incidents/list"
category: "Status Page"
writes_data: false
---
# JSM Ops - List incidents

**List incidents** — `GET /stakeholder-comms/cloudId/{cloudId}/api/incidents/list`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List incidents"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/incidents/list?cursor={{param:cursor}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `cursor` (query, string, optional) — Cursor for pagination.
- `limit` (query, string, optional) — Maximum number of incidents to return.

## Original description

List the incidents mentioned or updated on status page.
