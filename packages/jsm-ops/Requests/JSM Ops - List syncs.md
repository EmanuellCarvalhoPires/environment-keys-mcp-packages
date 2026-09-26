---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/syncs
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/syncs"
category: "Syncs"
writes_data: false
---
# JSM Ops - List syncs

**List syncs** — `GET /api/{cloudId}/v1/syncs`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List syncs"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/syncs?type={{param:type}}&teamId={{param:teamId}}&offset={{param:offset}}&size={{param:size}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `type` (query, string, optional) — Type of the sync. (For instance, "jira-software-cloud" for Jira Software Cloud Sync.)
- `teamId` (query, string, optional) — Id of the team that the syncs belongs to.
- `offset` (query, string, optional) — The offset parameter controls the starting point within the collection of resource results.
- `size` (query, string, optional) — The limit parameter controls the maximum number of items that may be returned for a single request.

## Original description

Lists syncs according to the provided filters.
- The user should have view permission for syncs.
