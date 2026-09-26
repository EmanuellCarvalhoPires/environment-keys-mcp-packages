---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_quick_filter
title: "JSW - Get quick filter"
kind: request
request: "[[JSW - Get quick filter]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/board/{boardId}/quickfilter/{quickFilterId} · Get quick filter. Returns the quick filter for a given quick filter ID. The quick filter will only be returned if the user can view the board that the quick filter belongs to. Writes data: no."
params:
  "boardId":
    type: string
    required: true
    description: "Value of boardId in the path."
  "quickFilterId":
    type: string
    required: true
    description: "The ID of the requested quick filter."
writes: false
expose: false
---
# jsw_get_quick_filter

`GET /rest/agile/1.0/board/{boardId}/quickfilter/{quickFilterId}` — Get quick filter

- Request: [[JSW - Get quick filter]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
