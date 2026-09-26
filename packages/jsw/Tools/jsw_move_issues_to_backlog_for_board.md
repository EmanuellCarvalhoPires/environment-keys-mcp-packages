---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/backlog
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSW]]"
tool: jsw_move_issues_to_backlog_for_board
title: "JSW - Move issues to backlog for board"
kind: request
request: "[[JSW - Move issues to backlog for board]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · POST /rest/agile/1.0/backlog/{boardId}/issue · Move issues to backlog for board. Move issues to the backlog of a particular board (if they are already on that board). Writes data: yes."
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
# jsw_move_issues_to_backlog_for_board

`POST /rest/agile/1.0/backlog/{boardId}/issue` — Move issues to backlog for board

- Request: [[JSW - Move issues to backlog for board]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
