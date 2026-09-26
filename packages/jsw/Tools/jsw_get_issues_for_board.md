---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_issues_for_board
title: "JSW - Get issues for board"
kind: request
request: "[[JSW - Get issues for board]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/board/{boardId}/issue · Get issues for board. Returns all issues from a board, for a given board ID. This only includes issues that the user has permission to view. An issue belongs to the board if its status is mapped to the board's column. Epic issues do not belongs to the scrum boards. Writes data: no."
params:
  "boardId":
    type: string
    required: true
    description: "The ID of the board that contains the requested issues."
  "startAt":
    type: string
    required: false
    description: "The starting index of the returned issues. Base index: 0. See the 'Pagination' section at the top of this page for more details."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of issues to return per page. See the 'Pagination' section at the top of this page for more details."
  "jql":
    type: string
    required: false
    description: "Filters results using a JQL query. If you define an order in your JQL query, it will override the default order of the returned issues."
  "validateQuery":
    type: string
    required: false
    description: "Specifies whether to validate the JQL query or not. Default: true."
  "fields":
    type: string
    required: false
    description: "The list of fields to return for each issue. By default, all navigable and Agile fields are returned."
  "expand":
    type: string
    required: false
    description: "This parameter is currently not used."
writes: false
expose: true
---
# jsw_get_issues_for_board

`GET /rest/agile/1.0/board/{boardId}/issue` — Get issues for board

- Request: [[JSW - Get issues for board]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
