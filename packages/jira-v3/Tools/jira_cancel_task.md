---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/tasks
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_cancel_task
title: "Jira v3 - Cancel task"
kind: request
request: "[[Jira v3 - Cancel task]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/task/{taskId}/cancel · Cancel task. Cancels a task. Permissions required: either of: Administer Jira global permission. Creator of the task. Writes data: yes."
params:
  "taskId":
    type: string
    required: true
    description: "The ID of the task."
writes: true
expose: false
---
# jira_cancel_task

`POST /rest/api/3/task/{taskId}/cancel` — Cancel task

- Request: [[Jira v3 - Cancel task]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
