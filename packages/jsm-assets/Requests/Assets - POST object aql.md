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
path: "/object/aql"
category: "Object"
writes_data: false
tool_note: "[[assets_post_object_aql]]"
---
# Assets - POST object aql

**/object/aql** — `POST /object/aql`

- Run by the tool [[assets_post_object_aql]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
POST https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/object/aql?startAt={{param:startAt}}&maxResults={{param:maxResults}}&includeAttributes={{param:includeAttributes}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `startAt` (query, string, optional) — The starting index for the next page of results
- `maxResults` (query, string, optional) — The maximum number of objects to return in this page of results. Actual number of results may be less, for example, if the last page of results is returned.
- `includeAttributes` (query, string, optional) — Should the objects attributes be included in the response. If this parameter is false only the information on the object will be returned and the object attributes will not be present
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "qlQuery": "objectType = Office AND Name LIKE SYD"
}
```

## Original description

Fetch Objects by AQL
