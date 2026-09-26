---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/backlog
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSW]]"
tool: jsw_move_issues_to_backlog
title: "JSW - Move issues to backlog"
kind: request
request: "[[JSW - Move issues to backlog]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · POST /rest/agile/1.0/backlog/issue · Move issues to backlog. Move issues to the backlog. This operation is equivalent to remove future and active sprints from a given set of issues. At most 50 issues may be moved at once. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsw_move_issues_to_backlog

`POST /rest/agile/1.0/backlog/issue` — Move issues to backlog

- Request: [[JSW - Move issues to backlog]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
