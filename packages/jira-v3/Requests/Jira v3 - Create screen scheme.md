---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/screen-schemes
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/screenscheme"
category: "Screen schemes"
writes_data: true
tool_note: "[[jira_create_screen_scheme]]"
---
# Jira v3 - Create screen scheme

**Create screen scheme** — `POST /rest/api/3/screenscheme`

- Run by the tool [[jira_create_screen_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/screenscheme
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "Manage employee data",
  "name": "Employee screen scheme",
  "screens": {
    "default": 10017,
    "edit": 10019,
    "view": 10020
  }
}
```

## Original description

Creates a screen scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
