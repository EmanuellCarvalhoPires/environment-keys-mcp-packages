---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-properties
  - api/operation/update
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: PUT
path: "/spaces/{space-id}/properties/{property-id}"
category: "Space Properties"
writes_data: true
tool_note: "[[confluence_update_space_property_by_id]]"
---
# Confluence v2 - Update space property by id

**Update space property by id** — `PUT /spaces/{space-id}/properties/{property-id}`

- Run by the tool [[confluence_update_space_property_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
PUT {{service.url}}/wiki/api/v2/spaces/{{param:space_id}}/properties/{{param:property_id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `space_id` (path, string, required) — The ID of the space the property belongs to.
- `property_id` (path, string, required) — The ID of the property to be updated.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update a space property by its id. 

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission) and 'Admin' permission for the space.
