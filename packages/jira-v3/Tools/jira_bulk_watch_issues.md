---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-bulk-operations
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_bulk_watch_issues
title: "Jira v3 - Bulk watch issues"
kind: request
request: "[[Jira v3 - Bulk watch issues]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/bulk/issues/watch · Bulk watch issues. Use this API to submit a bulk watch request. You can watch up to 1,000 issues in a single operation. Permissions required: Global bulk change permission. Browse project permission in all projects that contain the selected issues. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_bulk_watch_issues

`POST /rest/api/3/bulk/issues/watch` — Bulk watch issues

- Request: [[Jira v3 - Bulk watch issues]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
