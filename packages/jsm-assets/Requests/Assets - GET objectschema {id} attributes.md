---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/objectschema
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
app: "Assets"
method: GET
path: "/objectschema/{id}/attributes"
category: "Objectschema"
writes_data: false
tool_note: "[[assets_get_objectschema_attributes]]"
---
# Assets - GET objectschema {id} attributes

**/objectschema/{id}/attributes** — `GET /objectschema/{id}/attributes`

- Run by the tool [[assets_get_objectschema_attributes]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/objectschema/{{param:id}}/attributes?onlyValueEditable={{param:onlyValueEditable}}&extended={{param:extended}}&query={{param:query}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `onlyValueEditable` (query, string, optional) — Return only values that are associated with values that can be edited
- `extended` (query, string, optional) — Include the object type with each object type attribute
- `query` (query, string, optional) — A query that will be used to filter object type attributes by their name

## Original description

Find all object type attributes for this object schema
