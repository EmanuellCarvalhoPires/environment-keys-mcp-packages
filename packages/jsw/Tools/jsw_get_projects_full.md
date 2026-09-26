---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_projects_full
title: "JSW - Get projects full"
kind: request
request: "[[JSW - Get projects full]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/board/{boardId}/project/full · Get projects full. Returns all projects that are statically associated with the board, for the given board ID. Returned projects are ordered by the name. A project is associated with a board if the board filter contains reference the project. Writes data: no."
params:
  "boardId":
    type: string
    required: true
    description: "The ID of the board that contains returned projects."
writes: false
expose: false
---
# jsw_get_projects_full

`GET /rest/agile/1.0/board/{boardId}/project/full` — Get projects full

- Request: [[JSW - Get projects full]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
