---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_all_versions
title: "JSW - Get all versions"
kind: request
request: "[[JSW - Get all versions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/board/{boardId}/version · Get all versions. Returns all versions from a board, for a given board ID. This only includes versions that the user has permission to view. Note, if the user does not have permission to view the board, no versions will be returned at all. Writes data: no."
params:
  "boardId":
    type: string
    required: true
    description: "The ID of the board that contains the requested versions."
  "startAt":
    type: string
    required: false
    description: "The starting index of the returned versions. Base index: 0. See the 'Pagination' section at the top of this page for more details."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of versions to return per page. See the 'Pagination' section at the top of this page for more details."
  "released":
    type: string
    required: false
    description: "Filters results to versions that are either released or unreleased. Valid values: true, false."
writes: false
expose: false
---
# jsw_get_all_versions

`GET /rest/agile/1.0/board/{boardId}/version` — Get all versions

- Request: [[JSW - Get all versions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
