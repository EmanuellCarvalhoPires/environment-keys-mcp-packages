---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_approximate_issue_count_for_backlog
title: "JSW - Get approximate issue count for backlog"
kind: request
request: "[[JSW - Get approximate issue count for backlog]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/software/1.0/board/{boardId}/backlog/approximate-count · Get approximate issue count for backlog. Returns the approximate count of all issues from the board's backlog, for the given board ID. This is equivalent to counting the issues on all pages returned by Get issues for backlog enhanced. Recent updates might not be immediately visible in the returned output. Writes data: no."
params:
  "boardId":
    type: string
    required: true
    description: "The ID of the board that has the backlog containing the requested issues."
  "jql":
    type: string
    required: false
    description: "Filters results using a JQL query. Note that username and userkey can't be used as search terms for this parameter due to privacy reasons. Use accountId instead."
writes: false
expose: false
---
# jsw_get_approximate_issue_count_for_backlog

`GET /rest/software/1.0/board/{boardId}/backlog/approximate-count` — Get approximate issue count for backlog

- Request: [[JSW - Get approximate issue count for backlog]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
