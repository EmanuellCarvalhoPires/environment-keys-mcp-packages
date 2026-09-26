---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/long-running-task
  - api/operation/get
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_long_running_task
title: "Confluence v1 - Get long-running task"
kind: request
request: "[[Confluence v1 - Get long-running task]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/longtask/{id} · Get long-running task. Returns information about an active long-running task (e.g. space export), such as how long it has been running and the percentage of the task that has completed. Permissions required: Permission to access the Confluence site ('Can use' global permission). Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the task."
writes: false
expose: false
---
# confluence_v1_get_long_running_task

`GET /wiki/rest/api/longtask/{id}` — Get long-running task

- Request: [[Confluence v1 - Get long-running task]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
