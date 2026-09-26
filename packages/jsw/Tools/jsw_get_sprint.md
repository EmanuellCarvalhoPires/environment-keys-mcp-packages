---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/sprint
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_sprint
title: "JSW - Get sprint"
kind: request
request: "[[JSW - Get sprint]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/sprint/{sprintId} · Get sprint. Returns the sprint for a given sprint ID. The sprint will only be returned if the user can view the board that the sprint was created on, or view at least one of the issues in the sprint. Writes data: no."
params:
  "sprintId":
    type: string
    required: true
    description: "The ID of the requested sprint."
writes: false
expose: false
---
# jsw_get_sprint

`GET /rest/agile/1.0/sprint/{sprintId}` — Get sprint

- Request: [[JSW - Get sprint]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
