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
path: "/rest/agile/1.0/board/filter/{filterId}"
category: "Board"
writes_data: false
tool_note: "[[jsw_get_board_by_filter_id]]"
---
# JSW - Get board by filter id

**Get board by filter id** — `GET /rest/agile/1.0/board/filter/{filterId}`

- Run by the tool [[jsw_get_board_by_filter_id]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/board/filter/{{param:filterId}}?startAt={{param:startAt}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `filterId` (path, string, required) — Filters results to boards that are relevant to a filter. Not supported for next-gen boards.
- `startAt` (query, string, optional) — The starting index of the returned boards. Base index: 0. See the 'Pagination' section at the top of this page for more details.
- `maxResults` (query, string, optional) — The maximum number of boards to return per page. Default: 50. See the 'Pagination' section at the top of this page for more details.

## Original description

Returns any boards which use the provided filter id. This method can be executed by users without a valid software license in order to find which boards are using a particular filter.
