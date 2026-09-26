---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-bulk-operations
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_bulk_move_issues
title: "Jira v3 - Bulk move issues"
kind: request
request: "[[Jira v3 - Bulk move issues]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/bulk/issues/move · Bulk move issues. Use this API to submit a bulk issue move request. You can move multiple issues from multiple projects in a single request, but they must all be moved to a single project, issue type, and parent. You can't move more than 1000 issues (including subtasks) at once. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_bulk_move_issues

`POST /rest/api/3/bulk/issues/move` — Bulk move issues

- Request: [[Jira v3 - Bulk move issues]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
