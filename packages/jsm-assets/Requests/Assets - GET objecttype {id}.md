---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/objecttype
  - api/operation/get
  - api/effect/read
up: "[[MCP - Assets]]"
app: "Assets"
method: GET
path: "/objecttype/{id}"
category: "Objecttype"
writes_data: false
tool_note: "[[assets_get_objecttype]]"
---
# Assets - GET objecttype {id}

**/objecttype/{id}** — `GET /objecttype/{id}`

- Run by the tool [[assets_get_objecttype]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/objecttype/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Find an object type by id
