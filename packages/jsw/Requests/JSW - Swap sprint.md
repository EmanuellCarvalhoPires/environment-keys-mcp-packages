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
path: "/rest/agile/1.0/sprint/{sprintId}/swap"
category: "Sprint"
writes_data: true
tool_note: "[[jsw_swap_sprint]]"
---
# JSW - Swap sprint

**Swap sprint** — `POST /rest/agile/1.0/sprint/{sprintId}/swap`

- Run by the tool [[jsw_swap_sprint]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
POST {{service.url}}/rest/agile/1.0/sprint/{{param:sprintId}}/swap
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `sprintId` (path, string, required) — The ID of the sprint to swap.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "sprintToSwapWith": 3
}
```

## Original description

Swap the position of the sprint with the second sprint.
