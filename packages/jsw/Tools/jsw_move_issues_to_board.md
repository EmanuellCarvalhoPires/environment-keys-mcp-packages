---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSW]]"
tool: jsw_move_issues_to_board
title: "JSW - Move issues to board"
kind: request
request: "[[JSW - Move issues to board]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · POST /rest/agile/1.0/board/{boardId}/issue · Move issues to board. Move issues from the backog to the board (if they are already in the backlog of that board). Writes data: yes."
params:
  "boardId":
    type: string
    required: true
    description: "Value of boardId in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsw_move_issues_to_board

`POST /rest/agile/1.0/board/{boardId}/issue` — Move issues to board

- Request: [[JSW - Move issues to board]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
