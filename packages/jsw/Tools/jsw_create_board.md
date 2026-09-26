---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSW]]"
tool: jsw_create_board
title: "JSW - Create board"
kind: request
request: "[[JSW - Create board]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · POST /rest/agile/1.0/board · Create board. Creates a new board. Board name, type and filter ID is required. name \\- Must be less than 255 characters. type \\- Valid values: scrum, kanban filterId \\- ID of a filter that the user has permissions to view. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsw_create_board

`POST /rest/agile/1.0/board` — Create board

- Request: [[JSW - Create board]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
