---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/sprint
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSW]]"
tool: jsw_update_sprint
title: "JSW - Update sprint"
kind: request
request: "[[JSW - Update sprint]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · PUT /rest/agile/1.0/sprint/{sprintId} · Update sprint. Performs a full update of a sprint. A full update means that the result will be exactly the same as the request body. Any fields not present in the request JSON will be set to null. Writes data: yes."
params:
  "sprintId":
    type: string
    required: true
    description: "the ID of the sprint to update."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsw_update_sprint

`PUT /rest/agile/1.0/sprint/{sprintId}` — Update sprint

- Request: [[JSW - Update sprint]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
