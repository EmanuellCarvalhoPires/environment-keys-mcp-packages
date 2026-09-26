---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-priorities
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/priority/move"
category: "Issue priorities"
writes_data: true
tool_note: "[[jira_move_priorities]]"
---
# Jira v3 - Move priorities

**Move priorities** — `PUT /rest/api/3/priority/move`

- Run by the tool [[jira_move_priorities]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/priority/move
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "after": "10003",
  "ids": [
    "10004",
    "10005"
  ]
}
```

## Original description

Changes the order of issue priorities.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
