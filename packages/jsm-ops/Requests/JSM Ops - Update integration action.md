---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/integration-actions
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: PATCH
path: "/api/{cloudId}/v1/integrations/{integrationId}/actions/{id}"
category: "Integration actions"
writes_data: true
---
# JSM Ops - Update integration action

**Update integration action** — `PATCH /api/{cloudId}/v1/integrations/{integrationId}/actions/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Update integration action"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
PATCH https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/integrations/{{param:integrationId}}/actions/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `integrationId` (path, string, required) — ID of the integration.
- `id` (path, string, required) — ID of the integration action.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates an integration action.   **Permissions required:** Permission to update the integration action:
 - the user has read-only administrative right. 
 - the user is the admin of the team that the integration belongs to.
