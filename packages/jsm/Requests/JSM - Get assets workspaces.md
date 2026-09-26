---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/assets
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
app: "JSM"
method: GET
path: "/rest/servicedeskapi/assets/workspace"
category: "Assets"
writes_data: false
tool_note: "[[jsm_get_assets_workspaces]]"
---
# JSM - Get assets workspaces

**Get assets workspaces** — `GET /rest/servicedeskapi/assets/workspace`

- Run by the tool [[jsm_get_assets_workspaces]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
GET {{service.url}}/rest/servicedeskapi/assets/workspace?start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `start` (query, string, optional) — The starting index of the returned workspace IDs. Base index: 0 See the Pagination section for more details.
- `limit` (query, string, optional) — The maximum number of workspace IDs to return per page. Default: 50 See the Pagination section for more details.

## Original description

Returns a list of Assets workspace IDs. Include a workspace ID in the path to access the [Assets REST APIs](https://developer.atlassian.com/cloud/assets/rest).

**[Permissions](#permissions) required**: Any
