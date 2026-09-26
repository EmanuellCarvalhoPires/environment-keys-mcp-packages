---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSW]]"
tool: jsw_delete_board
title: "JSW - Delete board"
kind: request
request: "[[JSW - Delete board]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · DELETE /rest/agile/1.0/board/{boardId} · Delete board. Deletes the board. Admin without the view permission can still remove the board. Writes data: yes."
params:
  "boardId":
    type: string
    required: true
    description: "ID of the board to be deleted"
writes: true
expose: false
---
# jsw_delete_board

`DELETE /rest/agile/1.0/board/{boardId}` — Delete board

- Request: [[JSW - Delete board]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
