---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/sprint
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSW]]"
tool: jsw_swap_sprint
title: "JSW - Swap sprint"
kind: request
request: "[[JSW - Swap sprint]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · POST /rest/agile/1.0/sprint/{sprintId}/swap · Swap sprint. Swap the position of the sprint with the second sprint. Writes data: yes."
params:
  "sprintId":
    type: string
    required: true
    description: "The ID of the sprint to swap."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsw_swap_sprint

`POST /rest/agile/1.0/sprint/{sprintId}/swap` — Swap sprint

- Request: [[JSW - Swap sprint]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
