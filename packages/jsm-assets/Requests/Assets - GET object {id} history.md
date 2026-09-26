---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/object
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
app: "Assets"
method: GET
path: "/object/{id}/history"
category: "Object"
writes_data: false
tool_note: "[[assets_get_object_history]]"
---
# Assets - GET object {id} history

**/object/{id}/history** — `GET /object/{id}/history`

- Run by the tool [[assets_get_object_history]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/object/{{param:id}}/history?asc={{param:asc}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `asc` (query, string, optional) — Should the history be retrieved in ascending order

## Original description

Retrieve the history entries for this object
