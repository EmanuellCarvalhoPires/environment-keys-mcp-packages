---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/agile/1.0/board/{boardId}/version"
category: "Board"
writes_data: false
tool_note: "[[jsw_get_all_versions]]"
---
# JSW - Get all versions

**Get all versions** — `GET /rest/agile/1.0/board/{boardId}/version`

- Run by the tool [[jsw_get_all_versions]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/board/{{param:boardId}}/version?startAt={{param:startAt}}&maxResults={{param:maxResults}}&released={{param:released}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `boardId` (path, string, required) — The ID of the board that contains the requested versions.
- `startAt` (query, string, optional) — The starting index of the returned versions. Base index: 0. See the 'Pagination' section at the top of this page for more details.
- `maxResults` (query, string, optional) — The maximum number of versions to return per page. See the 'Pagination' section at the top of this page for more details.
- `released` (query, string, optional) — Filters results to versions that are either released or unreleased. Valid values: true, false.

## Original description

Returns all versions from a board, for a given board ID. This only includes versions that the user has permission to view. Note, if the user does not have permission to view the board, no versions will be returned at all. Returned versions are ordered by the name of the project from which they belong and then by sequence defined by user.
