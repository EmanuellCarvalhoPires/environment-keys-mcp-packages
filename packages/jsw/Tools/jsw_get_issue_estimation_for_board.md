---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/issue
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_issue_estimation_for_board
title: "JSW - Get issue estimation for board"
kind: request
request: "[[JSW - Get issue estimation for board]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/issue/{issueIdOrKey}/estimation · Get issue estimation for board. Returns the estimation of the issue and a fieldId of the field that is used for it. boardId param is required. This param determines which field will be updated on a issue. Original time internally stores and returns the estimation as a number of seconds. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the requested issue."
  "boardId":
    type: string
    required: false
    description: "The ID of the board required to determine which field is used for estimation."
writes: false
expose: false
---
# jsw_get_issue_estimation_for_board

`GET /rest/agile/1.0/issue/{issueIdOrKey}/estimation` — Get issue estimation for board

- Request: [[JSW - Get issue estimation for board]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
