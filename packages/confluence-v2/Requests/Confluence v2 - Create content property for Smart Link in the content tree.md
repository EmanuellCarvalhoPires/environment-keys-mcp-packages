---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-properties
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: POST
path: "/embeds/{id}/properties"
category: "Content Properties"
writes_data: true
tool_note: "[[confluence_create_content_property_for_smart_link_in_the_content]]"
---
# Confluence v2 - Create content property for Smart Link in the content tree

**Create content property for Smart Link in the content tree** — `POST /embeds/{id}/properties`

- Run by the tool [[confluence_create_content_property_for_smart_link_in_the_content]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/embeds/{{param:id}}/properties
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the Smart Link in the content tree to create a property for.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a new content property for a Smart Link in the content tree.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to update the Smart Link in the content tree.
