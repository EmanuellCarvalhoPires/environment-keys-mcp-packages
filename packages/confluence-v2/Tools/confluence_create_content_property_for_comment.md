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
tool: confluence_create_content_property_for_comment
title: "Confluence v2 - Create content property for comment"
kind: request
request: "[[Confluence v2 - Create content property for comment]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /comments/{comment-id}/properties · Create content property for comment. Creates a new content property for a comment. Permissions required: Permission to update the comment. Writes data: yes."
params:
  "comment_id":
    type: string
    required: true
    description: "The ID of the comment to create a property for."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_create_content_property_for_comment

`POST /comments/{comment-id}/properties` — Create content property for comment

- Request: [[Confluence v2 - Create content property for comment]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
