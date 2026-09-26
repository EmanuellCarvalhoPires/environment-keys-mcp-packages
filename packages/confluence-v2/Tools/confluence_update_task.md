---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/task
  - api/operation/update
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_update_task
title: "Confluence v2 - Update task"
kind: request
request: "[[Confluence v2 - Update task]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · PUT /tasks/{id} · Update task. Update a task by id. This endpoint currently only supports updating task status. Permissions required: Permission to edit the containing page or blog post and view its corresponding space. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the task to be updated. If you don't know the task ID, use Get tasks and filter the results."
  "body_format":
    type: string
    required: false
    description: "The content format types to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_update_task

`PUT /tasks/{id}` — Update task

- Request: [[Confluence v2 - Update task]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
