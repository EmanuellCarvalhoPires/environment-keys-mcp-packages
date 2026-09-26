---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/snippets
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_comment_on_a_snippet
title: "Bitbucket - Delete a comment on a snippet"
kind: request
request: "[[Bitbucket - Delete a comment on a snippet]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /snippets/{workspace}/{encoded_id}/comments/{comment_id} · Delete a comment on a snippet. Deletes a snippet comment. Comments can only be removed by the comment author, snippet creator, or workspace admin. Writes data: yes."
params:
  "encoded_id":
    type: string
    required: true
    description: "Value of encodedid in the path."
  "comment_id":
    type: string
    required: true
    description: "Value of commentid in the path."
writes: true
expose: false
---
# bitbucket_delete_a_comment_on_a_snippet

`DELETE /snippets/{workspace}/{encoded_id}/comments/{comment_id}` — Delete a comment on a snippet

- Request: [[Bitbucket - Delete a comment on a snippet]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
