---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/screens
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/screens/{screenId}/availableFields"
category: "Screens"
writes_data: false
tool_note: "[[jira_get_available_screen_fields]]"
---
# Jira v3 - Get available screen fields

**Get available screen fields** — `GET /rest/api/3/screens/{screenId}/availableFields`

- Run by the tool [[jira_get_available_screen_fields]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/screens/{{param:screenId}}/availableFields
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `screenId` (path, string, required) — The ID of the screen.

## Original description

Returns the fields that can be added to a tab on a screen.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
