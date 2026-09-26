---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-properties
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/custom-content/{custom-content-id}/properties/{property-id}"
category: "Content Properties"
writes_data: false
tool_note: "[[confluence_get_content_property_for_custom_content_by_id]]"
---
# Confluence v2 - Get content property for custom content by id

**Get content property for custom content by id** — `GET /custom-content/{custom-content-id}/properties/{property-id}`

- Run by the tool [[confluence_get_content_property_for_custom_content_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/custom-content/{{param:custom_content_id}}/properties/{{param:property_id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `custom_content_id` (path, string, required) — The ID of the custom content for which content properties should be returned.
- `property_id` (path, string, required) — The ID of the content property being requested.

## Original description

Retrieves a specific Content Property by ID that is attached to a specified custom content.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the page.
