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
path: "/rest/api/3/screens/addToDefault/{fieldId}"
category: "Screens"
writes_data: true
tool_note: "[[jira_add_field_to_default_screen]]"
---
# Jira v3 - Add field to default screen

**Add field to default screen** — `POST /rest/api/3/screens/addToDefault/{fieldId}`

- Run by the tool [[jira_add_field_to_default_screen]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/screens/addToDefault/{{param:fieldId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `fieldId` (path, string, required) — The ID of the field.

## Original description

Adds a field to the default tab of the default screen.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
