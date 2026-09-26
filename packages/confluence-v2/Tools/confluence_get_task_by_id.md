---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/task
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_task_by_id
title: "Confluence v2 - Get task by id"
kind: request
request: "[[Confluence v2 - Get task by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /tasks/{id} · Get task by id. Returns a specific task. Permissions required: Permission to view the containing page or blog post and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the task to be returned. If you don't know the task ID, use Get tasks and filter the results."
  "body_format":
    type: string
    required: false
    description: "The content format types to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field."
writes: false
expose: false
---
# confluence_get_task_by_id

`GET /tasks/{id}` — Get task by id

- Request: [[Confluence v2 - Get task by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
