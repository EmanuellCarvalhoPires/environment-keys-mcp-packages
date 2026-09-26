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
path: "/rest/agile/1.0/board/{boardId}/project/full"
category: "Board"
writes_data: false
tool_note: "[[jsw_get_projects_full]]"
---
# JSW - Get projects full

**Get projects full** — `GET /rest/agile/1.0/board/{boardId}/project/full`

- Run by the tool [[jsw_get_projects_full]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/board/{{param:boardId}}/project/full
Authorization: {{service.auth_token}}
```

## Parameters

- `boardId` (path, string, required) — The ID of the board that contains returned projects.

## Original description

Returns all projects that are statically associated with the board, for the given board ID. Returned projects are ordered by the name.

A project is associated with a board if the board filter contains reference the project.

The board filter contains reference the project only if JQL query guarantees that returned issues will be returned from the project set defined in JQL. For instance the query `project in (ABC, BCD) AND reporter = admin` have reference to ABC and BCD projects but query `project in (ABC, BCD) OR reporter = admin` doesn't have reference to any project.
