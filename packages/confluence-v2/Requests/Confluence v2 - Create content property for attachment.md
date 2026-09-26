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
path: "/attachments/{attachment-id}/properties"
category: "Content Properties"
writes_data: true
tool_note: "[[confluence_create_content_property_for_attachment]]"
---
# Confluence v2 - Create content property for attachment

**Create content property for attachment** — `POST /attachments/{attachment-id}/properties`

- Run by the tool [[confluence_create_content_property_for_attachment]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/attachments/{{param:attachment_id}}/properties
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `attachment_id` (path, string, required) — The ID of the attachment to create a property for.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a new content property for an attachment.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to update the attachment.
