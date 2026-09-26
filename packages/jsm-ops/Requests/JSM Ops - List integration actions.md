---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/integration-actions
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/integrations/{integrationId}/actions"
category: "Integration actions"
writes_data: false
---
# JSM Ops - List integration actions

**List integration actions** — `GET /api/{cloudId}/v1/integrations/{integrationId}/actions`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List integration actions"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/integrations/{{param:integrationId}}/actions?type={{param:type}}&direction={{param:direction}}&domain={{param:domain}}&name={{param:name}}&offset={{param:offset}}&size={{param:size}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `integrationId` (path, string, required) — Value of integrationId in the path.
- `type` (query, string, optional) — Type of the integration action.
- `direction` (query, string, optional) — Direction of the action. It can be incoming or outgoing
- `domain` (query, string, optional) — Domain of the action. It can be alert
- `name` (query, string, optional) — Name of the integration action.
- `offset` (query, string, optional) — The index of the first item to return in a page of results.
- `size` (query, string, optional) — The maximum number of items to return per page.

## Original description

Lists integration actions of an integration that user can view.   **Permissions required:** Permission to get the integration action: 
 - the user has read-only administrative right. 
 - the integration's assigned team is one of the teams that the user belongs to.
