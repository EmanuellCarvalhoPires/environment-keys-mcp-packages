---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/comment
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_delete_footer_comment
title: "Confluence v2 - Delete footer comment"
kind: request
request: "[[Confluence v2 - Delete footer comment]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · DELETE /footer-comments/{comment-id} · Delete footer comment. Deletes a footer comment. This is a permanent deletion and cannot be reverted. Permissions required: Permission to view the content of the page or blogpost and its corresponding space. Permission to delete comments in the space. Writes data: yes."
params:
  "comment_id":
    type: string
    required: true
    description: "The ID of the comment to be retrieved."
writes: true
expose: false
---
# confluence_delete_footer_comment

`DELETE /footer-comments/{comment-id}` — Delete footer comment

- Request: [[Confluence v2 - Delete footer comment]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
