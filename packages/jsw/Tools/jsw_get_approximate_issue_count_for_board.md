---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_approximate_issue_count_for_board
title: "JSW - Get approximate issue count for board"
kind: request
request: "[[JSW - Get approximate issue count for board]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/software/1.0/board/{boardId}/issue/approximate-count · Get approximate issue count for board. Returns the approximate count of all issues from a board, for a given board ID. This is equivalent to counting the issues on all pages returned by Get issues for board enhanced. Recent updates might not be immediately visible in the returned output. Writes data: no."
params:
  "boardId":
    type: string
    required: true
    description: "The ID of the board that contains the requested issues."
  "jql":
    type: string
    required: false
    description: "Filters results using a JQL query. Note that username and userkey can't be used as search terms for this parameter due to privacy reasons. Use accountId instead."
writes: false
expose: false
---
# jsw_get_approximate_issue_count_for_board

`GET /rest/software/1.0/board/{boardId}/issue/approximate-count` — Get approximate issue count for board

- Request: [[JSW - Get approximate issue count for board]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
