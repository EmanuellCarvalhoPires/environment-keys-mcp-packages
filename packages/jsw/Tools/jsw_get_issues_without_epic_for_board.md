---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_issues_without_epic_for_board
title: "JSW - Get issues without epic for board"
kind: request
request: "[[JSW - Get issues without epic for board]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/board/{boardId}/epic/none/issue · Get issues without epic for board. Returns all issues that do not belong to any epic on a board, for a given board ID. This only includes issues that the user has permission to view. Issues returned from this resource include Agile fields, like sprint, closedSprints, flagged, and epic. Writes data: no."
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
    description: "A comma-separated list of the parameters to expand."
writes: false
expose: false
---
# jsw_get_issues_without_epic_for_board

`GET /rest/agile/1.0/board/{boardId}/epic/none/issue` — Get issues without epic for board

- Request: [[JSW - Get issues without epic for board]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
