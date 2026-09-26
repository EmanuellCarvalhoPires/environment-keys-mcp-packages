---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/integrations
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: DELETE
path: "/api/{cloudId}/v1/integrations/{id}"
category: "Integrations"
writes_data: true
---
# JSM Ops - Delete integration

**Delete integration** — `DELETE /api/{cloudId}/v1/integrations/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete integration"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/integrations/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Deletes an integration.   **Permissions required:** Permission to delete the integration:
 - the user has read-only administrative right. 
 - the user is the admin of the team that the integration belongs to.
