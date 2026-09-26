---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/integrations
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: PATCH
path: "/api/{cloudId}/v1/integrations/{id}"
category: "Integrations"
writes_data: true
---
# JSM Ops - Update integration

**Update integration** — `PATCH /api/{cloudId}/v1/integrations/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Update integration"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
PATCH https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/integrations/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates an integration.    **Permissions required:** Permission to update the integration:
 - the user has read-only administrative right. 
 - the user is the admin of the team that the integration belongs to.
