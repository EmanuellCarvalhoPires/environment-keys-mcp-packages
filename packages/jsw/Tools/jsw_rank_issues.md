---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/issue
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSW]]"
tool: jsw_rank_issues
title: "JSW - Rank issues"
kind: request
request: "[[JSW - Rank issues]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · PUT /rest/agile/1.0/issue/rank · Rank issues. Moves (ranks) issues before or after a given issue. At most 50 issues may be ranked at once. This operation may fail for some issues, although this will be rare. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsw_rank_issues

`PUT /rest/agile/1.0/issue/rank` — Rank issues

- Request: [[JSW - Rank issues]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
