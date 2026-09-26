---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-attachments
  - api/operation/update
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: PUT
path: "/wiki/rest/api/content/{id}/child/attachment/{attachmentId}"
category: "Content - attachments"
writes_data: true
tool_note: "[[confluence_v1_update_attachment_properties]]"
---
# Confluence v1 - Update attachment properties

**Update attachment properties** — `PUT /wiki/rest/api/content/{id}/child/attachment/{attachmentId}`

- Run by the tool [[confluence_v1_update_attachment_properties]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
PUT {{service.url}}/wiki/rest/api/content/{{param:id}}/child/attachment/{{param:attachmentId}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the content that the attachment is attached to.
- `attachmentId` (path, string, required) — The ID of the attachment to update.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates the attachment properties, i.e. the non-binary data of an attachment
like the filename, media-type, comment, and parent container.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to update the content.
