---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/field-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/config/fieldschemes/{id}"
category: "Field schemes"
writes_data: true
tool_note: "[[jira_update_field_scheme]]"
---
# Jira v3 - Update field scheme

**Update field scheme** — `PUT /rest/api/3/config/fieldschemes/{id}`

- Run by the tool [[jira_update_field_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/config/fieldschemes/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "Field association scheme description",
  "name": "Field association scheme name"
}
```

## Original description

Endpoint for updating an existing field association scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
