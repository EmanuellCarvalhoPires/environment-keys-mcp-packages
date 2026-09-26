---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-properties
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: POST
path: "/spaces/{space-id}/properties"
category: "Space Properties"
writes_data: true
tool_note: "[[confluence_create_space_property_in_space]]"
---
# Confluence v2 - Create space property in space

**Create space property in space** — `POST /spaces/{space-id}/properties`

- Run by the tool [[confluence_create_space_property_in_space]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/spaces/{{param:space_id}}/properties
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `space_id` (path, string, required) — The ID of the space for which space properties should be returned.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a new space property.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission) and 'Admin' permission for the space.
