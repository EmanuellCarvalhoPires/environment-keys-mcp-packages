---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-bulk-operations
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_bulk_issue_operation_progress
title: "Jira v3 - Get bulk issue operation progress"
kind: request
request: "[[Jira v3 - Get bulk issue operation progress]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/bulk/queue/{taskId} · Get bulk issue operation progress. Use this to get the progress state for the specified bulk operation taskId. Permissions required: Global bulk change permission. Writes data: no."
params:
  "taskId":
    type: string
    required: true
    description: "The ID of the task."
writes: false
expose: false
---
# jira_get_bulk_issue_operation_progress

`GET /rest/api/3/bulk/queue/{taskId}` — Get bulk issue operation progress

- Request: [[Jira v3 - Get bulk issue operation progress]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
