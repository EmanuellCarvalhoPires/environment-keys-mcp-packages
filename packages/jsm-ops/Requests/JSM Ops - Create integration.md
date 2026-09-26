---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/integrations
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/integrations"
category: "Integrations"
writes_data: true
---
# JSM Ops - Create integration

**Create integration** — `POST /api/{cloudId}/v1/integrations`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Create integration"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/integrations
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates an integration. It can be team or global integration by using teamId in the payload.
  
 **Permissions required:** Permission to create an integration:
 - the user has edit configuration right. 
 - the user is the admin of the team that the integration belongs to. 
  
 *Slack* and *Microsoft Teams* types of integration are not supported for this operation.
