---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-priorities
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_move_priorities
title: "Jira v3 - Move priorities"
kind: request
request: "[[Jira v3 - Move priorities]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/priority/move · Move priorities. Changes the order of issue priorities. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_move_priorities

`PUT /rest/api/3/priority/move` — Move priorities

- Request: [[Jira v3 - Move priorities]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
