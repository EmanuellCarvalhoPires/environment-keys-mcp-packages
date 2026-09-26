---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/objecttype
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
app: "Assets"
method: GET
path: "/objecttype/{id}/attributes"
category: "Objecttype"
writes_data: false
tool_note: "[[assets_get_objecttype_attributes]]"
---
# Assets - GET objecttype {id} attributes

**/objecttype/{id}/attributes** — `GET /objecttype/{id}/attributes`

- Run by the tool [[assets_get_objecttype_attributes]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/objecttype/{{param:id}}/attributes?onlyValueEditable={{param:onlyValueEditable}}&orderByName={{param:orderByName}}&query={{param:query}}&includeValuesExist={{param:includeValuesExist}}&excludeParentAttributes={{param:excludeParentAttributes}}&includeChildren={{param:includeChildren}}&orderByRequired={{param:orderByRequired}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `onlyValueEditable` (query, string, optional) — Query parameter onlyValueEditable.
- `orderByName` (query, string, optional) — Query parameter orderByName.
- `query` (query, string, optional) — Query parameter query.
- `includeValuesExist` (query, string, optional) — Query parameter includeValuesExist.
- `excludeParentAttributes` (query, string, optional) — Query parameter excludeParentAttributes.
- `includeChildren` (query, string, optional) — Query parameter includeChildren.
- `orderByRequired` (query, string, optional) — Query parameter orderByRequired.

## Original description

Find all attributes for this object type
