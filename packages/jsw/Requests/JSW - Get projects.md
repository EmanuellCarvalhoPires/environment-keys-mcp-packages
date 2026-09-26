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
path: "/rest/agile/1.0/board/{boardId}/project"
category: "Board"
writes_data: false
tool_note: "[[jsw_get_projects]]"
---
# JSW - Get projects

**Get projects** — `GET /rest/agile/1.0/board/{boardId}/project`

- Run by the tool [[jsw_get_projects]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/board/{{param:boardId}}/project?startAt={{param:startAt}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `boardId` (path, string, required) — The ID of the board that contains returned projects.
- `startAt` (query, string, optional) — The starting index of the returned projects. Base index: 0. See the 'Pagination' section at the top of this page for more details.
- `maxResults` (query, string, optional) — The maximum number of projects to return per page. See the 'Pagination' section at the top of this page for more details.

## Original description

Returns all projects that are associated with the board, for the given board ID. If the user does not have permission to view the board, no projects will be returned at all. Returned projects are ordered by the name.

A project is associated with a board if the board filter contains reference the project or there is an issue from the project that belongs to the board.

The board filter contains reference the project only if JQL query guarantees that returned issues will be returned from the project set defined in JQL. For instance the query `project in (ABC, BCD) AND reporter = admin` have reference to ABC and BCD projects but query `project in (ABC, BCD) OR reporter = admin` doesn't have reference to any project.

An issue belongs to the board if its status is mapped to the board's column. Epic issues do not belongs to the scrum boards.
