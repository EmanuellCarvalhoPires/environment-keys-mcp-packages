---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-properties
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: DELETE
path: "/spaces/{space-id}/properties/{property-id}"
category: "Space Properties"
writes_data: true
tool_note: "[[confluence_delete_space_property_by_id]]"
---
# Confluence v2 - Delete space property by id

**Delete space property by id** — `DELETE /spaces/{space-id}/properties/{property-id}`

- Run by the tool [[confluence_delete_space_property_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
DELETE {{service.url}}/wiki/api/v2/spaces/{{param:space_id}}/properties/{{param:property_id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `space_id` (path, string, required) — The ID of the space the property belongs to.
- `property_id` (path, string, required) — The ID of the property to be deleted.

## Original description

Deletes a space property by its id. 

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission) and 'Admin' permission for the space.
