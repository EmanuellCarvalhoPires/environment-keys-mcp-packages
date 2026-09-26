---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_reports_for_board
title: "JSW - Get reports for board"
kind: request
request: "[[JSW - Get reports for board]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/board/{boardId}/reports · Get reports for board. Writes data: no."
params:
  "boardId":
    type: string
    required: true
    description: "Value of boardId in the path."
writes: false
expose: false
---
# jsw_get_reports_for_board

`GET /rest/agile/1.0/board/{boardId}/reports` — Get reports for board

- Request: [[JSW - Get reports for board]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
