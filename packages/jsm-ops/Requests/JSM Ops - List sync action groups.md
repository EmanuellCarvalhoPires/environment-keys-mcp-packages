---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/sync-action-groups
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/syncs/{syncId}/action-groups"
category: "Sync action groups"
writes_data: false
---
# JSM Ops - List sync action groups

**List sync action groups** — `GET /api/{cloudId}/v1/syncs/{syncId}/action-groups`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List sync action groups"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/syncs/{{param:syncId}}/action-groups?type={{param:type}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `syncId` (path, string, required) — Id of the sync
- `type` (query, string, optional) — Type of the action group.

## Original description

Lists sync action groups of a sync
