---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/sprint
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSW]]"
app: "JSW"
method: DELETE
path: "/rest/agile/1.0/sprint/{sprintId}"
category: "Sprint"
writes_data: true
tool_note: "[[jsw_delete_sprint]]"
---
# JSW - Delete sprint

**Delete sprint** — `DELETE /rest/agile/1.0/sprint/{sprintId}`

- Run by the tool [[jsw_delete_sprint]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
DELETE {{service.url}}/rest/agile/1.0/sprint/{{param:sprintId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `sprintId` (path, string, required) — The ID of the sprint to delete.

## Original description

Deletes a sprint. Once a sprint is deleted, all open issues in the sprint will be moved to the backlog.
