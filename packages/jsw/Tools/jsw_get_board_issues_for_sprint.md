---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_board_issues_for_sprint
title: "JSW - Get board issues for sprint"
kind: request
request: "[[JSW - Get board issues for sprint]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/board/{boardId}/sprint/{sprintId}/issue · Get board issues for sprint. Get all issues you have access to that belong to the sprint from the board. Issue returned from this resource contains additional fields like: sprint, closedSprints, flagged and epic. Issues are returned ordered by rank. JQL order has higher priority than default rank. Writes data: no."
params:
  "boardId":
    type: string
    required: true
    description: "The ID of the board that contains requested issues."
  "sprintId":
    type: string
    required: true
    description: "The ID of the sprint that contains requested issues."
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
    description: "A comma-separated list of the parameters to expand."
writes: false
expose: false
---
# jsw_get_board_issues_for_sprint

`GET /rest/agile/1.0/board/{boardId}/sprint/{sprintId}/issue` — Get board issues for sprint

- Request: [[JSW - Get board issues for sprint]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
