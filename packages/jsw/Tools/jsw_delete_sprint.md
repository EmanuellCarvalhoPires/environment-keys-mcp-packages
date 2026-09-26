---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/sprint
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSW]]"
tool: jsw_delete_sprint
title: "JSW - Delete sprint"
kind: request
request: "[[JSW - Delete sprint]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · DELETE /rest/agile/1.0/sprint/{sprintId} · Delete sprint. Deletes a sprint. Once a sprint is deleted, all open issues in the sprint will be moved to the backlog. Writes data: yes."
params:
  "sprintId":
    type: string
    required: true
    description: "The ID of the sprint to delete."
writes: true
expose: false
---
# jsw_delete_sprint

`DELETE /rest/agile/1.0/sprint/{sprintId}` — Delete sprint

- Request: [[JSW - Delete sprint]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
