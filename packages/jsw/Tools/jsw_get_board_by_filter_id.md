---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_board_by_filter_id
title: "JSW - Get board by filter id"
kind: request
request: "[[JSW - Get board by filter id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/board/filter/{filterId} · Get board by filter id. Returns any boards which use the provided filter id. This method can be executed by users without a valid software license in order to find which boards are using a particular filter. Writes data: no."
params:
  "filterId":
    type: string
    required: true
    description: "Filters results to boards that are relevant to a filter. Not supported for next-gen boards."
  "startAt":
    type: string
    required: false
    description: "The starting index of the returned boards. Base index: 0. See the 'Pagination' section at the top of this page for more details."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of boards to return per page. Default: 50. See the 'Pagination' section at the top of this page for more details."
writes: false
expose: false
---
# jsw_get_board_by_filter_id

`GET /rest/agile/1.0/board/filter/{filterId}` — Get board by filter id

- Request: [[JSW - Get board by filter id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
