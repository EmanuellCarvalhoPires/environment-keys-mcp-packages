---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/integration-actions
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: DELETE
path: "/api/{cloudId}/v1/integrations/{integrationId}/actions/{id}"
category: "Integration actions"
writes_data: true
---
# JSM Ops - Delete integration action

**Delete integration action** — `DELETE /api/{cloudId}/v1/integrations/{integrationId}/actions/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete integration action"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/integrations/{{param:integrationId}}/actions/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `integrationId` (path, string, required) — ID of the integration.
- `id` (path, string, required) — ID of the integration action.

## Original description

Deletes an integration action.   **Permissions required:** Permission to update integration alert filter:
 - the user has read-only administrative right. 
 - the user is the admin of the team that the integration belongs to.
