---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/epic
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSW]]"
tool: jsw_move_issues_to_epic
title: "JSW - Move issues to epic"
kind: request
request: "[[JSW - Move issues to epic]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · POST /rest/agile/1.0/epic/{epicIdOrKey}/issue · Move issues to epic. Moves issues to an epic, for a given epic id. Issues can be only in a single epic at the same time. That means that already assigned issues to an epic, will not be assigned to the previous epic anymore. Writes data: yes."
params:
  "epicIdOrKey":
    type: string
    required: true
    description: "The id or key of the epic that you want to assign issues to."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsw_move_issues_to_epic

`POST /rest/agile/1.0/epic/{epicIdOrKey}/issue` — Move issues to epic

- Request: [[JSW - Move issues to epic]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
