---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_board
title: "JSW - Get board"
kind: request
request: "[[JSW - Get board]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/board/{boardId} · Get board. Returns the board for the given board ID. This board will only be returned if the user has permission to view it. Admins without the view permission will see the board as a private one, so will see only a subset of the board's data (board location for instance). Writes data: no."
params:
  "boardId":
    type: string
    required: true
    description: "The ID of the requested board."
writes: false
expose: false
---
# jsw_get_board

`GET /rest/agile/1.0/board/{boardId}` — Get board

- Request: [[JSW - Get board]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
