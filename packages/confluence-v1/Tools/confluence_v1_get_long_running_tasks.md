---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/long-running-task
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_long_running_tasks
title: "Confluence v1 - Get long-running tasks"
kind: request
request: "[[Confluence v1 - Get long-running tasks]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/longtask · Get long-running tasks. Returns information about all active long-running tasks (e.g. space export), such as how long each task has been running and the percentage of each task that has completed. Permissions required: Permission to access the Confluence site ('Can use' global permission). Writes data: no."
params:
  "key":
    type: string
    required: false
    description: "The key of the tasks."
  "start":
    type: string
    required: false
    description: "The starting index of the returned tasks."
  "limit":
    type: string
    required: false
    description: "The maximum number of tasks to return per page. Note, this may be restricted by fixed system limits."
writes: false
expose: false
---
# confluence_v1_get_long_running_tasks

`GET /wiki/rest/api/longtask` — Get long-running tasks

- Request: [[Confluence v1 - Get long-running tasks]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
