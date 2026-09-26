---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/sprint
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSW]]"
tool: jsw_move_issues_to_sprint_and_rank
title: "JSW - Move issues to sprint and rank"
kind: request
request: "[[JSW - Move issues to sprint and rank]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · POST /rest/agile/1.0/sprint/{sprintId}/issue · Move issues to sprint and rank. Moves issues to a sprint, for a given sprint ID. Issues can only be moved to open or active sprints. The maximum number of issues that can be moved in one operation is 50. Writes data: yes."
params:
  "sprintId":
    type: string
    required: true
    description: "The ID of the sprint that you want to assign issues to."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsw_move_issues_to_sprint_and_rank

`POST /rest/agile/1.0/sprint/{sprintId}/issue` — Move issues to sprint and rank

- Request: [[JSW - Move issues to sprint and rank]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
