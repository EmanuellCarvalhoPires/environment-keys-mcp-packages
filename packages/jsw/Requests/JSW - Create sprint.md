---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/sprint
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSW]]"
app: "JSW"
method: POST
path: "/rest/agile/1.0/sprint"
category: "Sprint"
writes_data: true
tool_note: "[[jsw_create_sprint]]"
---
# JSW - Create sprint

**Create sprint** — `POST /rest/agile/1.0/sprint`

- Run by the tool [[jsw_create_sprint]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
POST {{service.url}}/rest/agile/1.0/sprint
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "endDate": "2015-04-20T01:22:00.000+10:00",
  "goal": "sprint 1 goal",
  "name": "sprint 1",
  "originBoardId": 5,
  "startDate": "2015-04-11T15:22:00.000+10:00"
}
```

## Original description

Creates a future sprint. Sprint name and origin board id are required. Start date, end date, and goal are optional.

Note that the sprint name is trimmed. Also, when starting sprints from the UI, the "endDate" set through this call is ignored and instead the last sprint's duration is used to fill the form.
