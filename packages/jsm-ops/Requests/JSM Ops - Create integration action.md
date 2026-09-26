---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/integration-actions
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/integrations/{integrationId}/actions"
category: "Integration actions"
writes_data: true
---
# JSM Ops - Create integration action

**Create integration action** — `POST /api/{cloudId}/v1/integrations/{integrationId}/actions`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Create integration action"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/integrations/{{param:integrationId}}/actions
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `integrationId` (path, string, required) — ID of the integration
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates an integration action.  **Permissions required:** Permission to create an integration action: 
 - the user has read-only administrative right. 
 - the user is the admin of the team that the integration belongs to.
