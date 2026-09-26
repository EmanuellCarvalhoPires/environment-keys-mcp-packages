---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_bulk_fetch_issues
title: "Jira v3 - Bulk fetch issues"
kind: request
request: "[[Jira v3 - Bulk fetch issues]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/issue/bulkfetch · Bulk fetch issues. Returns the details for a set of requested issues. By default you can request up to 100 issues in a single call. Writes data: no."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_bulk_fetch_issues

`POST /rest/api/3/issue/bulkfetch` — Bulk fetch issues

- Request: [[Jira v3 - Bulk fetch issues]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
