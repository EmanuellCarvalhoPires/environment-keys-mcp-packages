---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/screen-tabs
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/screens/{screenId}/tabs"
category: "Screen tabs"
writes_data: true
tool_note: "[[jira_create_screen_tab]]"
---
# Jira v3 - Create screen tab

**Create screen tab** — `POST /rest/api/3/screens/{screenId}/tabs`

- Run by the tool [[jira_create_screen_tab]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/screens/{{param:screenId}}/tabs
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
  "name": "Fields Tab"
}
```

## Original description

Creates a tab for a screen.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
