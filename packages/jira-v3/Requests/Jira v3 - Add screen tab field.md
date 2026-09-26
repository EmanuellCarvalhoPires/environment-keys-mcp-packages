---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/screen-tab-fields
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/screens/{screenId}/tabs/{tabId}/fields"
category: "Screen tab fields"
writes_data: true
tool_note: "[[jira_add_screen_tab_field]]"
---
# Jira v3 - Add screen tab field

**Add screen tab field** — `POST /rest/api/3/screens/{screenId}/tabs/{tabId}/fields`

- Run by the tool [[jira_add_screen_tab_field]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/screens/{{param:screenId}}/tabs/{{param:tabId}}/fields?skipFieldAssociation={{param:skipFieldAssociation}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `screenId` (path, string, required) — The ID of the screen.
- `tabId` (path, string, required) — The ID of the screen tab.
- `skipFieldAssociation` (query, string, optional) — Query parameter skipFieldAssociation.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "fieldId": "summary"
}
```

## Original description

Adds a field to a screen tab.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
