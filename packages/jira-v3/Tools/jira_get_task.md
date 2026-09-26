---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/tasks
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_task
title: "Jira v3 - Get task"
kind: request
request: "[[Jira v3 - Get task]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/task/{taskId} · Get task. Returns the status of a long-running asynchronous task. When a task has finished, this operation returns the JSON blob applicable to the task. See the documentation of the operation that created the task for details. Task details are not permanently retained. Writes data: no."
params:
  "taskId":
    type: string
    required: true
    description: "The ID of the task."
writes: false
expose: false
---
# jira_get_task

`GET /rest/api/3/task/{taskId}` — Get task

- Request: [[Jira v3 - Get task]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
