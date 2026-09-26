---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/epic
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSW]]"
app: "JSW"
method: POST
path: "/rest/agile/1.0/epic/{epicIdOrKey}/issue"
category: "Epic"
writes_data: true
tool_note: "[[jsw_move_issues_to_epic]]"
---
# JSW - Move issues to epic

**Move issues to epic** — `POST /rest/agile/1.0/epic/{epicIdOrKey}/issue`

- Run by the tool [[jsw_move_issues_to_epic]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
POST {{service.url}}/rest/agile/1.0/epic/{{param:epicIdOrKey}}/issue
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `epicIdOrKey` (path, string, required) — The id or key of the epic that you want to assign issues to.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "issues": [
    "10001",
    "PR-1",
    "PR-3"
  ]
}
```

## Original description

Moves issues to an epic, for a given epic id. Issues can be only in a single epic at the same time. That means that already assigned issues to an epic, will not be assigned to the previous epic anymore. The user needs to have the edit issue permission for all issue they want to move and to the epic. The maximum number of issues that can be moved in one operation is 50. **Note:** This operation does not work for epics in next-gen projects.
