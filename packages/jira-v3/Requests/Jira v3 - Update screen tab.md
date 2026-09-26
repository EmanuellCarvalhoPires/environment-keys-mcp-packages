---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/screen-tabs
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/screens/{screenId}/tabs/{tabId}"
category: "Screen tabs"
writes_data: true
tool_note: "[[jira_update_screen_tab]]"
---
# Jira v3 - Update screen tab

**Update screen tab** — `PUT /rest/api/3/screens/{screenId}/tabs/{tabId}`

- Run by the tool [[jira_update_screen_tab]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/screens/{{param:screenId}}/tabs/{{param:tabId}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `screenId` (path, string, required) — The ID of the screen.
- `tabId` (path, string, required) — The ID of the screen tab.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates the name of a screen tab.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
