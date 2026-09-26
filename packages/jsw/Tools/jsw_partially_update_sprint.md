---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/sprint
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSW]]"
tool: jsw_partially_update_sprint
title: "JSW - Partially update sprint"
kind: request
request: "[[JSW - Partially update sprint]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · POST /rest/agile/1.0/sprint/{sprintId} · Partially update sprint. Performs a partial update of a sprint. A partial update means that fields not present in the request JSON will not be updated. Notes: For closed sprints, only the name and goal can be updated; changes to other fields will be ignored. Writes data: yes."
params:
  "sprintId":
    type: string
    required: true
    description: "The ID of the sprint to update."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsw_partially_update_sprint

`POST /rest/agile/1.0/sprint/{sprintId}` — Partially update sprint

- Request: [[JSW - Partially update sprint]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
