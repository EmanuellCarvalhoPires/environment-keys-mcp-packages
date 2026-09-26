---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/screen-tab-fields
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}"
category: "Screen tab fields"
writes_data: true
tool_note: "[[jira_remove_screen_tab_field]]"
---
# Jira v3 - Remove screen tab field

**Remove screen tab field** — `DELETE /rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}`

- Run by the tool [[jira_remove_screen_tab_field]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/screens/{{param:screenId}}/tabs/{{param:tabId}}/fields/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `screenId` (path, string, required) — The ID of the screen.
- `tabId` (path, string, required) — The ID of the screen tab.
- `id` (path, string, required) — The ID of the field.

## Original description

Removes a field from a screen tab.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
