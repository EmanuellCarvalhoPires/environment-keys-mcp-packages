---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-properties
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/spaces/{space-id}/properties/{property-id}"
category: "Space Properties"
writes_data: false
tool_note: "[[confluence_get_space_property_by_id]]"
---
# Confluence v2 - Get space property by id

**Get space property by id** — `GET /spaces/{space-id}/properties/{property-id}`

- Run by the tool [[confluence_get_space_property_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/spaces/{{param:space_id}}/properties/{{param:property_id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `space_id` (path, string, required) — The ID of the space the property belongs to.
- `property_id` (path, string, required) — The ID of the property to be retrieved.

## Original description

Retrieve a space property by its id. 

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission) and 'View' permission for the space.
