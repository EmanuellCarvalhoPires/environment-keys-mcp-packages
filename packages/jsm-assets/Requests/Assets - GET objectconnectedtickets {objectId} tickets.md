---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/objectconnectedtickets
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
app: "Assets"
method: GET
path: "/objectconnectedtickets/{objectId}/tickets"
category: "Objectconnectedtickets"
writes_data: false
tool_note: "[[assets_get_objectconnectedtickets_tickets]]"
---
# Assets - GET objectconnectedtickets {objectId} tickets

**/objectconnectedtickets/{objectId}/tickets** — `GET /objectconnectedtickets/{objectId}/tickets`

- Run by the tool [[assets_get_objectconnectedtickets_tickets]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/objectconnectedtickets/{{param:objectId}}/tickets
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `objectId` (path, string, required) — Value of objectId in the path.

## Original description

Relation between Jira issues and Assets objects
