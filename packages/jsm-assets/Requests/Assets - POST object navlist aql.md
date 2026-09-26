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
path: "/object/navlist/aql"
category: "Object"
writes_data: false
tool_note: "[[assets_post_object_navlist_aql]]"
---
# Assets - POST object navlist aql

**/object/navlist/aql** — `POST /object/navlist/aql`

- Run by the tool [[assets_post_object_navlist_aql]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
POST https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/object/navlist/aql
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
  "objectTypeId": "23",
  "attributesToDisplay": {
    "attributesToDisplayIds": [
      "135",
      "144"
    ]
  },
  "page": 1,
  "asc": 1,
  "resultsPerPage": 25,
  "includeAttributes": false,
  "objectSchemaId": "6",
  "qlQuery": "objectType = Office AND Name LIKE SYD"
}
```

## Original description

Retrieve a list of objects based on an AQL. Deprecated from 30 September 2024. Please use POST /object/aql instead. For more information please see https://developer.atlassian.com/changelog/#CHANGE-1661.
