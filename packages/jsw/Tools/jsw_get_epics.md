---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_epics
title: "JSW - Get epics"
kind: request
request: "[[JSW - Get epics]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/board/{boardId}/epic · Get epics. Returns all epics from the board, for the given board ID. This only includes epics that the user has permission to view. Note, if the user does not have permission to view the board, no epics will be returned at all. Writes data: no."
params:
  "boardId":
    type: string
    required: true
    description: "The ID of the board that contains the requested epics."
  "startAt":
    type: string
    required: false
    description: "The starting index of the returned epics. Base index: 0. See the 'Pagination' section at the top of this page for more details."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of epics to return per page. See the 'Pagination' section at the top of this page for more details."
  "done":
    type: string
    required: false
    description: "Filters results to epics that are either done or not done. Valid values: true, false."
writes: false
expose: false
---
# jsw_get_epics

`GET /rest/agile/1.0/board/{boardId}/epic` — Get epics

- Request: [[JSW - Get epics]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
