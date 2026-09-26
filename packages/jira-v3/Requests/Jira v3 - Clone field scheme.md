---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/field-schemes
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/config/fieldschemes/{id}/clone"
category: "Field schemes"
writes_data: true
tool_note: "[[jira_clone_field_scheme]]"
---
# Jira v3 - Clone field scheme

**Clone field scheme** — `POST /rest/api/3/config/fieldschemes/{id}/clone`

- Run by the tool [[jira_clone_field_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/config/fieldschemes/{{param:id}}/clone
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the source field association scheme to clone from
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "Field association scheme description",
  "name": "Field association scheme name"
}
```

## Original description

Endpoint for cloning an existing field association scheme into a new one.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
