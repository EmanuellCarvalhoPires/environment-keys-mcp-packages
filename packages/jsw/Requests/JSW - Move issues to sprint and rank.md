---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/sprint
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSW]]"
app: "JSW"
method: POST
path: "/rest/agile/1.0/sprint/{sprintId}/issue"
category: "Sprint"
writes_data: true
tool_note: "[[jsw_move_issues_to_sprint_and_rank]]"
---
# JSW - Move issues to sprint and rank

**Move issues to sprint and rank** — `POST /rest/agile/1.0/sprint/{sprintId}/issue`

- Run by the tool [[jsw_move_issues_to_sprint_and_rank]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
POST {{service.url}}/rest/agile/1.0/sprint/{{param:sprintId}}/issue
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `sprintId` (path, string, required) — The ID of the sprint that you want to assign issues to.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "issues": [
    "PR-1",
    "10001",
    "PR-3"
  ],
  "rankBeforeIssue": "PR-4",
  "rankCustomFieldId": 10521
}
```

## Original description

Moves issues to a sprint, for a given sprint ID. Issues can only be moved to open or active sprints. The maximum number of issues that can be moved in one operation is 50.
