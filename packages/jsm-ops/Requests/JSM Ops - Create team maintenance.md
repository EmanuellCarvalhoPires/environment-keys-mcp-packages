---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/maintenances
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/teams/{teamId}/maintenances"
category: "Maintenances"
writes_data: true
---
# JSM Ops - Create team maintenance

**Create team maintenance** — `POST /api/{cloudId}/v1/teams/{teamId}/maintenances`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Create team maintenance"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/maintenances
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `teamId` (path, string, required) — Identifier of the maintenance owning team.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

This endpoint is used to create a new maintenance for a specific team in Jira Service Management. The maintenance plan can include various rules that enable or disable multiple entities like policies, integrations or syncs. Please note that integrations and syncs cannot be enabled via a maintenance plan but policies can.
