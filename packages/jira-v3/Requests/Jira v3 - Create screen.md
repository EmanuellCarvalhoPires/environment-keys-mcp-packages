---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/screens
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/screens"
category: "Screens"
writes_data: true
tool_note: "[[jira_create_screen]]"
---
# Jira v3 - Create screen

**Create screen** — `POST /rest/api/3/screens`

- Run by the tool [[jira_create_screen]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/screens
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "Enables changes to resolution and linked issues.",
  "name": "Resolve Security Issue Screen"
}
```

## Original description

Creates a screen with a default field tab.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
