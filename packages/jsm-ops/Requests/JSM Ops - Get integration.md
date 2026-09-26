---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/integrations
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/integrations/{id}"
category: "Integrations"
writes_data: false
---
# JSM Ops - Get integration

**Get integration** — `GET /api/{cloudId}/v1/integrations/{id}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get integration"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/integrations/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — ID of the integration.

## Original description

Returns the integration details.   **Permissions required:** Permission to access to the integration: 
 - the user has read-only administrative right. 
 - the integration's assigned team is one of the teams that the user belongs to.
