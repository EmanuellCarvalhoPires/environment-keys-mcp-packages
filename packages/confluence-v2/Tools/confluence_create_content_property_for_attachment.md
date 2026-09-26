---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-properties
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_create_content_property_for_attachment
title: "Confluence v2 - Create content property for attachment"
kind: request
request: "[[Confluence v2 - Create content property for attachment]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /attachments/{attachment-id}/properties · Create content property for attachment. Creates a new content property for an attachment. Permissions required: Permission to update the attachment. Writes data: yes."
params:
  "attachment_id":
    type: string
    required: true
    description: "The ID of the attachment to create a property for."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_create_content_property_for_attachment

`POST /attachments/{attachment-id}/properties` — Create content property for attachment

- Request: [[Confluence v2 - Create content property for attachment]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
