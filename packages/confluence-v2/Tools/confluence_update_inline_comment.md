---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/comment
  - api/operation/update
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_update_inline_comment
title: "Confluence v2 - Update inline comment"
kind: request
request: "[[Confluence v2 - Update inline comment]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · PUT /inline-comments/{comment-id} · Update inline comment. Update an inline comment. This can be used to update the body text of a comment and/or to resolve the comment Permissions required: Permission to view the content of the page or blogpost and its corresponding space. Permission to create comments in the space. Writes data: yes."
params:
  "comment_id":
    type: string
    required: true
    description: "The ID of the comment to be retrieved."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_update_inline_comment

`PUT /inline-comments/{comment-id}` — Update inline comment

- Request: [[Confluence v2 - Update inline comment]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
