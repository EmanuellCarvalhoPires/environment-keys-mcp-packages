---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-attachments
  - api/operation/update
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_update_attachment_properties
title: "Confluence v1 - Update attachment properties"
kind: request
request: "[[Confluence v1 - Update attachment properties]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · PUT /wiki/rest/api/content/{id}/child/attachment/{attachmentId} · Update attachment properties. Updates the attachment properties, i.e. the non-binary data of an attachment like the filename, media-type, comment, and parent container. Permissions required: Permission to update the content. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the content that the attachment is attached to."
  "attachmentId":
    type: string
    required: true
    description: "The ID of the attachment to update."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_update_attachment_properties

`PUT /wiki/rest/api/content/{id}/child/attachment/{attachmentId}` — Update attachment properties

- Request: [[Confluence v1 - Update attachment properties]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
