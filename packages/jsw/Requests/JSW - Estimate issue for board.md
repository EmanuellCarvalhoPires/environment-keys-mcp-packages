---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/issue
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSW]]"
app: "JSW"
method: PUT
path: "/rest/agile/1.0/issue/{issueIdOrKey}/estimation"
category: "Issue"
writes_data: true
tool_note: "[[jsw_estimate_issue_for_board]]"
---
# JSW - Estimate issue for board

**Estimate issue for board** — `PUT /rest/agile/1.0/issue/{issueIdOrKey}/estimation`

- Run by the tool [[jsw_estimate_issue_for_board]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
PUT {{service.url}}/rest/agile/1.0/issue/{{param:issueIdOrKey}}/estimation?boardId={{param:boardId}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the requested issue.
- `boardId` (query, string, optional) — The ID of the board required to determine which field is used for estimation.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "value": "8.0"
}
```

## Original description

Updates the estimation of the issue. boardId param is required. This param determines which field will be updated on a issue.

Note that this resource changes the estimation field of the issue regardless of appearance the field on the screen.

Original time tracking estimation field accepts estimation in formats like "1w", "2d", "3h", "20m" or number which represent number of minutes. However, internally the field stores and returns the estimation as a number of seconds.

The field used for estimation on the given board can be obtained from [board configuration resource](#agile/1.0/board-getConfiguration). More information about the field are returned by [edit meta resource](#api-rest-api-3-issue-issueIdOrKey-editmeta-get) or [field resource](#api-rest-api-3-field-get).
