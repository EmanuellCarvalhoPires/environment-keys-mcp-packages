---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/screen-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/screenscheme/{screenSchemeId}"
category: "Screen schemes"
writes_data: true
tool_note: "[[jira_update_screen_scheme]]"
---
# Jira v3 - Update screen scheme

**Update screen scheme** — `PUT /rest/api/3/screenscheme/{screenSchemeId}`

- Run by the tool [[jira_update_screen_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/screenscheme/{{param:screenSchemeId}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `screenSchemeId` (path, string, required) — The ID of the screen scheme.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "name": "Employee screen scheme v2",
  "screens": {
    "create": "10019",
    "default": "10018"
  }
}
```

## Original description

Updates a screen scheme. Only screen schemes used in classic projects can be updated.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
