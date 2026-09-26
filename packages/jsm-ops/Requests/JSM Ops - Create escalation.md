---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/escalations
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/teams/{teamId}/escalations"
category: "Escalations"
writes_data: true
---
# JSM Ops - Create escalation

**Create escalation** — `POST /api/{cloudId}/v1/teams/{teamId}/escalations`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Create escalation"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/escalations
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `teamId` (path, string, required) — Identifier of the escalation owning team.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "name": "FE Daily On-call Escalation",
  "description": "",
  "rules": [
    {
      "condition": "if-not-acked",
      "notifyType": "default",
      "delay": 5,
      "recipient": {
        "id": "f0f07a3d-bde8-4b2a-8d3e-f97020a51e32",
        "type": "team"
      }
    }
  ],
  "enabled": true,
  "repeat": {
    "waitInterval": 10,
    "count": 5,
    "resetRecipientStates": true,
    "closeAlertAfterAll": true
  }
}
```

## Original description

Creates an escalation with the given properties.
