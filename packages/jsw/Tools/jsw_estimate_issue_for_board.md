---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/issue
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSW]]"
tool: jsw_estimate_issue_for_board
title: "JSW - Estimate issue for board"
kind: request
request: "[[JSW - Estimate issue for board]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · PUT /rest/agile/1.0/issue/{issueIdOrKey}/estimation · Estimate issue for board. Updates the estimation of the issue. boardId param is required. This param determines which field will be updated on a issue. Note that this resource changes the estimation field of the issue regardless of appearance the field on the screen. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the requested issue."
  "boardId":
    type: string
    required: false
    description: "The ID of the board required to determine which field is used for estimation."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsw_estimate_issue_for_board

`PUT /rest/agile/1.0/issue/{issueIdOrKey}/estimation` — Estimate issue for board

- Request: [[JSW - Estimate issue for board]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
