---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/comment
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_create_footer_comment
title: "Confluence v2 - Create footer comment"
kind: request
request: "[[Confluence v2 - Create footer comment]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /footer-comments · Create footer comment. Create a footer comment. The footer comment can be made against several locations: - at the top level (specifying pageId or blogPostId in the request body) - as a reply (specifying parentCommentId in the request body) - against an attachment (note: this is different than the comm… Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_create_footer_comment

`POST /footer-comments` — Create footer comment

- Request: [[Confluence v2 - Create footer comment]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
