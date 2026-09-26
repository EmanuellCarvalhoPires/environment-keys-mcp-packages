---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_all_quick_filters
title: "JSW - Get all quick filters"
kind: request
request: "[[JSW - Get all quick filters]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/board/{boardId}/quickfilter · Get all quick filters. Returns all quick filters from a board, for a given board ID. Writes data: no."
params:
  "boardId":
    type: string
    required: true
    description: "The ID of the board that contains the requested quick filters."
  "startAt":
    type: string
    required: false
    description: "The starting index of the returned quick filters. Base index: 0. See the 'Pagination' section at the top of this page for more details."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of sprints to return per page. See the 'Pagination' section at the top of this page for more details."
writes: false
expose: false
---
# jsw_get_all_quick_filters

`GET /rest/agile/1.0/board/{boardId}/quickfilter` — Get all quick filters

- Request: [[JSW - Get all quick filters]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
