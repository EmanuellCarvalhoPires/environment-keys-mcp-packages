---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/objectschema
  - api/operation/get
  - api/effect/read
up: "[[MCP - Assets]]"
app: "Assets"
method: GET
path: "/objectschema/{id}"
category: "Objectschema"
writes_data: false
tool_note: "[[assets_get_objectschema]]"
---
# Assets - GET objectschema {id}

**/objectschema/{id}** — `GET /objectschema/{id}`

- Run by the tool [[assets_get_objectschema]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/objectschema/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Find a schema by id
