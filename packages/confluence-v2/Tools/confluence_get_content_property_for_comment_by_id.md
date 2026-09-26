---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-properties
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_content_property_for_comment_by_id
title: "Confluence v2 - Get content property for comment by id"
kind: request
request: "[[Confluence v2 - Get content property for comment by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /comments/{comment-id}/properties/{property-id} · Get content property for comment by id. Retrieves a specific Content Property by ID that is attached to a specified comment. Permissions required: Permission to view the comment. Writes data: no."
params:
  "comment_id":
    type: string
    required: true
    description: "The ID of the comment for which content properties should be returned."
  "property_id":
    type: string
    required: true
    description: "The ID of the content property being requested."
writes: false
expose: false
---
# confluence_get_content_property_for_comment_by_id

`GET /comments/{comment-id}/properties/{property-id}` — Get content property for comment by id

- Request: [[Confluence v2 - Get content property for comment by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
