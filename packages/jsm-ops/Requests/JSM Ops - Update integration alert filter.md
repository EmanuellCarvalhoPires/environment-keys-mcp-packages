---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/integration-outgoing-filters
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: PATCH
path: "/api/{cloudId}/v1/integrations/{integrationId}/outgoing/alert-filter/main"
category: "Integration outgoing filters"
writes_data: true
---
# JSM Ops - Update integration alert filter

**Update integration alert filter** — `PATCH /api/{cloudId}/v1/integrations/{integrationId}/outgoing/alert-filter/main`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Update integration alert filter"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
PATCH https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/integrations/{{param:integrationId}}/outgoing/alert-filter/main
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `integrationId` (path, string, required) — Value of integrationId in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "conditionMatchType": "match-all",
  "conditions": []
}
```

## Original description

Updates Integration outgoing alert filter.   **Permissions required:** Permission to update integration alert filter:
 - the user has read-only administrative right. 
 - the user is the admin of the team that the integration belongs to.
