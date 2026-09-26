---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_all_sprints
title: "JSW - Get all sprints"
kind: request
request: "[[JSW - Get all sprints]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/board/{boardId}/sprint · Get all sprints. Returns all sprints from a board, for a given board ID. This only includes sprints that the user has permission to view. Writes data: no."
params:
  "boardId":
    type: string
    required: true
    description: "The ID of the board that contains the requested sprints."
  "startAt":
    type: string
    required: false
    description: "The starting index of the returned sprints. Base index: 0. See the 'Pagination' section at the top of this page for more details."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of sprints to return per page. See the 'Pagination' section at the top of this page for more details."
  "state":
    type: string
    required: false
    description: "Filters results to sprints in specified states. Valid values: future, active, closed. You can define multiple states separated by commas, e.g. state=active,closed"
writes: false
expose: true
---
# jsw_get_all_sprints

`GET /rest/agile/1.0/board/{boardId}/sprint` — Get all sprints

- Request: [[JSW - Get all sprints]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
