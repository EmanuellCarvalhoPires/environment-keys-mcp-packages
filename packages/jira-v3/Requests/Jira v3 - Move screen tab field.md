---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/screen-tab-fields
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}/move"
category: "Screen tab fields"
writes_data: true
tool_note: "[[jira_move_screen_tab_field]]"
---
# Jira v3 - Move screen tab field

**Move screen tab field** — `POST /rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}/move`

- Run by the tool [[jira_move_screen_tab_field]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/screens/{{param:screenId}}/tabs/{{param:tabId}}/fields/{{param:id}}/move
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `screenId` (path, string, required) — The ID of the screen.
- `tabId` (path, string, required) — The ID of the screen tab.
- `id` (path, string, required) — The ID of the field.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Moves a screen tab field.

If `after` and `position` are provided in the request, `position` is ignored.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
