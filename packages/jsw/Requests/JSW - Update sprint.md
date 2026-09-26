---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/sprint
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSW]]"
app: "JSW"
method: PUT
path: "/rest/agile/1.0/sprint/{sprintId}"
category: "Sprint"
writes_data: true
tool_note: "[[jsw_update_sprint]]"
---
# JSW - Update sprint

**Update sprint** — `PUT /rest/agile/1.0/sprint/{sprintId}`

- Run by the tool [[jsw_update_sprint]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
PUT {{service.url}}/rest/agile/1.0/sprint/{{param:sprintId}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `sprintId` (path, string, required) — the ID of the sprint to update.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "completeDate": "2015-04-20T11:11:28.008+10:00",
  "endDate": "2015-04-16T14:01:00.000+10:00",
  "goal": "sprint 1 goal",
  "name": "sprint 1",
  "startDate": "2015-04-11T15:36:00.000+10:00",
  "state": "closed"
}
```

## Original description

Performs a full update of a sprint. A full update means that the result will be exactly the same as the request body. Any fields not present in the request JSON will be set to null.

Notes:

 *  For closed sprints, only the name and goal can be updated; changes to other fields will be ignored.
 *  A sprint can be started by updating the state to 'active'. This requires the sprint to be in the 'future' state and have a startDate and endDate set.
 *  A sprint can be completed by updating the state to 'closed'. This action requires the sprint to be in the 'active' state. This sets the completeDate to the time of the request.
 *  Other changes to state are not allowed.
 *  The completeDate field cannot be updated manually.
