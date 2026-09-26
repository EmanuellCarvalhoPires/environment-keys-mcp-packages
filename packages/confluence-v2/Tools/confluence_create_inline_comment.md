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
tool: confluence_create_inline_comment
title: "Confluence v2 - Create inline comment"
kind: request
request: "[[Confluence v2 - Create inline comment]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /inline-comments · Create inline comment. Create an inline comment. This can be at the top level (specifying pageId or blogPostId in the request body) or as a reply (specifying parentCommentId in the request body). Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_create_inline_comment

`POST /inline-comments` — Create inline comment

- Request: [[Confluence v2 - Create inline comment]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
