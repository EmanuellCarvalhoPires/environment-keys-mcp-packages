---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/screen-tabs
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/screens/{screenId}/tabs/{tabId}"
category: "Screen tabs"
writes_data: true
tool_note: "[[jira_delete_screen_tab]]"
---
# Jira v3 - Delete screen tab

**Delete screen tab** — `DELETE /rest/api/3/screens/{screenId}/tabs/{tabId}`

- Run by the tool [[jira_delete_screen_tab]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/screens/{{param:screenId}}/tabs/{{param:tabId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `screenId` (path, string, required) — The ID of the screen.
- `tabId` (path, string, required) — The ID of the screen tab.

## Original description

Deletes a screen tab.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
