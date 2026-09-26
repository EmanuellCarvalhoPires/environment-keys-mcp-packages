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
path: "/objectschema/list"
category: "Objectschema"
writes_data: false
tool_note: "[[assets_get_objectschema_list]]"
---
# Assets - GET objectschema list

**/objectschema/list** — `GET /objectschema/list`

- Run by the tool [[assets_get_objectschema_list]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/objectschema/list?startAt={{param:startAt}}&maxResults={{param:maxResults}}&includeCounts={{param:includeCounts}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The starting index for the next page of results
- `maxResults` (query, string, optional) — The maximum number of objects to return in this page of results. Actual number of results may be less, for example, if the last page of results is returned.
- `includeCounts` (query, string, optional) — Should the object and object type count for schema be included in the response. If this parameter is false, object and object type count will return 0.

## Original description

Resource to find object schemas in Assets
