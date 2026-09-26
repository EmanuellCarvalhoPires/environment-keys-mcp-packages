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
path: "/rest/agile/1.0/sprint/{sprintId}"
category: "Sprint"
writes_data: true
tool_note: "[[jsw_partially_update_sprint]]"
---
# JSW - Partially update sprint

**Partially update sprint** — `POST /rest/agile/1.0/sprint/{sprintId}`

- Run by the tool [[jsw_partially_update_sprint]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
POST {{service.url}}/rest/agile/1.0/sprint/{{param:sprintId}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `sprintId` (path, string, required) — The ID of the sprint to update.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "name": "new name"
}
```

## Original description

Performs a partial update of a sprint. A partial update means that fields not present in the request JSON will not be updated.

Notes:

 *  For closed sprints, only the name and goal can be updated; changes to other fields will be ignored.
 *  A sprint can be started by updating the state to 'active'. This requires the sprint to be in the 'future' state and have a startDate and endDate set.
 *  A sprint can be completed by updating the state to 'closed'. This action requires the sprint to be in the 'active' state. This sets the completeDate to the time of the request.
 *  Other changes to state are not allowed.
 *  The completeDate field cannot be updated manually.
