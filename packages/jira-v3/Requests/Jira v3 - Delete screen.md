---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/screens
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/screens/{screenId}"
category: "Screens"
writes_data: true
tool_note: "[[jira_delete_screen]]"
---
# Jira v3 - Delete screen

**Delete screen** — `DELETE /rest/api/3/screens/{screenId}`

- Run by the tool [[jira_delete_screen]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/screens/{{param:screenId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `screenId` (path, string, required) — The ID of the screen.

## Original description

Deletes a screen. A screen cannot be deleted if it is used in a screen scheme, workflow, or workflow draft.

Only screens used in classic projects can be deleted.
