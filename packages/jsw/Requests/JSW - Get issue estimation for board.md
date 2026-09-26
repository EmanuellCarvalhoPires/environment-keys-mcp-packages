---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/issue
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/agile/1.0/issue/{issueIdOrKey}/estimation"
category: "Issue"
writes_data: false
tool_note: "[[jsw_get_issue_estimation_for_board]]"
---
# JSW - Get issue estimation for board

**Get issue estimation for board** — `GET /rest/agile/1.0/issue/{issueIdOrKey}/estimation`

- Run by the tool [[jsw_get_issue_estimation_for_board]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/issue/{{param:issueIdOrKey}}/estimation?boardId={{param:boardId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the requested issue.
- `boardId` (query, string, optional) — The ID of the board required to determine which field is used for estimation.

## Original description

Returns the estimation of the issue and a fieldId of the field that is used for it. `boardId` param is required. This param determines which field will be updated on a issue.

Original time internally stores and returns the estimation as a number of seconds.

The field used for estimation on the given board can be obtained from [board configuration resource](#agile/1.0/board-getConfiguration). More information about the field are returned by [edit meta resource](#api-rest-api-3-issue-getEditIssueMeta) or [field resource](#api-rest-api-3-field-get).
