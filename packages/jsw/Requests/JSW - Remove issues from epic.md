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
path: "/rest/agile/1.0/epic/none/issue"
category: "Epic"
writes_data: true
tool_note: "[[jsw_remove_issues_from_epic]]"
---
# JSW - Remove issues from epic

**Remove issues from epic** — `POST /rest/agile/1.0/epic/none/issue`

- Run by the tool [[jsw_remove_issues_from_epic]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
POST {{service.url}}/rest/agile/1.0/epic/none/issue
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

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

Removes issues from epics. The user needs to have the edit issue permission for all issue they want to remove from epics. The maximum number of issues that can be moved in one operation is 50. **Note:** This operation does not work for epics in next-gen projects. Instead, update the issue using `\{ fields: \{ parent: \{\} \} \}`
