---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/agile/1.0/board/{boardId}/quickfilter/{quickFilterId}"
category: "Board"
writes_data: false
tool_note: "[[jsw_get_quick_filter]]"
---
# JSW - Get quick filter

**Get quick filter** — `GET /rest/agile/1.0/board/{boardId}/quickfilter/{quickFilterId}`

- Run by the tool [[jsw_get_quick_filter]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/board/{{param:boardId}}/quickfilter/{{param:quickFilterId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `boardId` (path, string, required) — Value of boardId in the path.
- `quickFilterId` (path, string, required) — The ID of the requested quick filter.

## Original description

Returns the quick filter for a given quick filter ID. The quick filter will only be returned if the user can view the board that the quick filter belongs to.
