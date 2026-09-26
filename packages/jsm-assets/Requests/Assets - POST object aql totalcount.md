---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/object
  - api/operation/search
  - api/effect/read
up: "[[MCP - Assets]]"
app: "Assets"
method: POST
path: "/object/aql/totalcount"
category: "Object"
writes_data: false
tool_note: "[[assets_post_object_aql_totalcount]]"
---
# Assets - POST object aql totalcount

**/object/aql/totalcount** — `POST /object/aql/totalcount`

- Run by the tool [[assets_post_object_aql_totalcount]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
POST https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/object/aql/totalcount
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "qlQuery": "objectType = Office AND Name LIKE SYD"
}
```

## Original description

This API provides the total count of objects that match a specified AQL query. Please note that this operation may incur performance latency.
