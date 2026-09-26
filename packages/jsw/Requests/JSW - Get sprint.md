---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/sprint
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/agile/1.0/sprint/{sprintId}"
category: "Sprint"
writes_data: false
tool_note: "[[jsw_get_sprint]]"
---
# JSW - Get sprint

**Get sprint** — `GET /rest/agile/1.0/sprint/{sprintId}`

- Run by the tool [[jsw_get_sprint]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/sprint/{{param:sprintId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `sprintId` (path, string, required) — The ID of the requested sprint.

## Original description

Returns the sprint for a given sprint ID. The sprint will only be returned if the user can view the board that the sprint was created on, or view at least one of the issues in the sprint.
