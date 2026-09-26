---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/sprint
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSW]]"
tool: jsw_create_sprint
title: "JSW - Create sprint"
kind: request
request: "[[JSW - Create sprint]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · POST /rest/agile/1.0/sprint · Create sprint. Creates a future sprint. Sprint name and origin board id are required. Start date, end date, and goal are optional. Note that the sprint name is trimmed. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsw_create_sprint

`POST /rest/agile/1.0/sprint` — Create sprint

- Request: [[JSW - Create sprint]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
