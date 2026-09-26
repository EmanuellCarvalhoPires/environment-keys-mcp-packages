---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/integration-actions
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/integrations/{integrationId}/actions/{id}"
category: "Integration actions"
writes_data: false
---
# JSM Ops - Get integration action

**Get integration action** — `GET /api/{cloudId}/v1/integrations/{integrationId}/actions/{id}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get integration action"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/integrations/{{param:integrationId}}/actions/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `integrationId` (path, string, required) — ID of the integration.
- `id` (path, string, required) — ID of the integration action.

## Original description

Returns the action of an integration.   **Permissions required:** Permission to access to the integration action: 
 - the user has read-only administrative right. 
 - the integration's assigned team is one of the teams that the user belongs to.
