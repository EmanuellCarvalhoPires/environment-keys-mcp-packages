---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/integration-outgoing-filters
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/integrations/{integrationId}/outgoing/alert-filter/main"
category: "Integration outgoing filters"
writes_data: false
---
# JSM Ops - Get integration alert filter

**Get integration alert filter** — `GET /api/{cloudId}/v1/integrations/{integrationId}/outgoing/alert-filter/main`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get integration alert filter"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/integrations/{{param:integrationId}}/outgoing/alert-filter/main
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `integrationId` (path, string, required) — Value of integrationId in the path.

## Original description

Returns the outgoing alert filter details of an integration.   **Permissions required:** Permission to access to the integration outgoing alert filter: 
 - the user has read-only administrative right. 
 - the integration's assigned team is one of the teams that the user belongs to.
