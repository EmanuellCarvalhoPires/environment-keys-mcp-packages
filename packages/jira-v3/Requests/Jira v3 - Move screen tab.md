---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/screen-tabs
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/screens/{screenId}/tabs/{tabId}/move/{pos}"
category: "Screen tabs"
writes_data: true
tool_note: "[[jira_move_screen_tab]]"
---
# Jira v3 - Move screen tab

**Move screen tab** — `POST /rest/api/3/screens/{screenId}/tabs/{tabId}/move/{pos}`

- Run by the tool [[jira_move_screen_tab]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/screens/{{param:screenId}}/tabs/{{param:tabId}}/move/{{param:pos}}
Authorization: {{service.auth_token}}
```

## Parameters

- `screenId` (path, string, required) — The ID of the screen.
- `tabId` (path, string, required) — The ID of the screen tab.
- `pos` (path, string, required) — The position of tab. The base index is 0.

## Original description

Moves a screen tab.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
