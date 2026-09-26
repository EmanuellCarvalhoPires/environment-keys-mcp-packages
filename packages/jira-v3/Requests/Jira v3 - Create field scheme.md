---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/field-schemes
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/config/fieldschemes"
category: "Field schemes"
writes_data: true
tool_note: "[[jira_create_field_scheme]]"
---
# Jira v3 - Create field scheme

**Create field scheme** — `POST /rest/api/3/config/fieldschemes`

- Run by the tool [[jira_create_field_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/config/fieldschemes
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "Field association scheme description",
  "name": "Field association scheme name"
}
```

## Original description

Endpoint for creating a new field association scheme.

A new scheme is **not** copied from, or based on, any existing field association scheme. Instead, it is initialised with a minimal default set of critical fields sourced from the instance's own *system* and *product* fields (the fields returned by the product's field API), rather than from a scheme you specify.

To create a scheme that is based on an existing one, use the *Clone field scheme* endpoint instead.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
