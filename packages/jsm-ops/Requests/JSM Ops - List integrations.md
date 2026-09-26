---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/integrations
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/integrations"
category: "Integrations"
writes_data: false
---
# JSM Ops - List integrations

**List integrations** — `GET /api/{cloudId}/v1/integrations`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List integrations"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/integrations?type={{param:type}}&teamId={{param:teamId}}&name={{param:name}}&offset={{param:offset}}&size={{param:size}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `type` (query, string, optional) — Type of the integration.
- `teamId` (query, string, optional) — ID of the team that integration belongs to.
- `name` (query, string, optional) — Name of the integration.
- `offset` (query, string, optional) — The index of the first item to return in a page of results.
- `size` (query, string, optional) — The maximum number of items to return per page.

## Original description

Returns all integrations that user can view.   **Permissions required:** Permission to access Jira Service Management; however, the list contains an integration if: 
 - the user has read-only administrative right. 
 - the integration's assigned team is one of the teams that the user belongs to.
