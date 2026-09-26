---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/screens
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/screens/{screenId}"
category: "Screens"
writes_data: true
tool_note: "[[jira_update_screen]]"
---
# Jira v3 - Update screen

**Update screen** — `PUT /rest/api/3/screens/{screenId}`

- Run by the tool [[jira_update_screen]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/screens/{{param:screenId}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `screenId` (path, string, required) — The ID of the screen.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "Enables changes to resolution and linked issues for accessibility related issues.",
  "name": "Resolve Accessibility Issue Screen"
}
```

## Original description

Updates a screen. Only screens used in classic projects can be updated.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
