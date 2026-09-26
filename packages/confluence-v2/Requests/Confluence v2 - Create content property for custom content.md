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
path: "/custom-content/{custom-content-id}/properties"
category: "Content Properties"
writes_data: true
tool_note: "[[confluence_create_content_property_for_custom_content]]"
---
# Confluence v2 - Create content property for custom content

**Create content property for custom content** — `POST /custom-content/{custom-content-id}/properties`

- Run by the tool [[confluence_create_content_property_for_custom_content]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/custom-content/{{param:custom_content_id}}/properties
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `custom_content_id` (path, string, required) — The ID of the custom content to create a property for.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a new content property for a piece of custom content.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to update the custom content.
