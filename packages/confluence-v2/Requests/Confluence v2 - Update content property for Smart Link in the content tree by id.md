---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-properties
  - api/operation/update
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: PUT
path: "/embeds/{embed-id}/properties/{property-id}"
category: "Content Properties"
writes_data: true
tool_note: "[[confluence_update_content_property_for_smart_link_in_the_content]]"
---
# Confluence v2 - Update content property for Smart Link in the content tree by id

**Update content property for Smart Link in the content tree by id** — `PUT /embeds/{embed-id}/properties/{property-id}`

- Run by the tool [[confluence_update_content_property_for_smart_link_in_the_content]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
PUT {{service.url}}/wiki/api/v2/embeds/{{param:embed_id}}/properties/{{param:property_id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `embed_id` (path, string, required) — The ID of the Smart Link in the content tree the property belongs to.
- `property_id` (path, string, required) — The ID of the property to be updated.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update a content property for a Smart Link in the content tree by its id. 

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to edit the Smart Link in the content tree.
