---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-bulk-operations
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_bulk_edit_issues
title: "Jira v3 - Bulk edit issues"
kind: request
request: "[[Jira v3 - Bulk edit issues]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/bulk/issues/fields · Bulk edit issues. Use this API to submit a bulk edit request and simultaneously edit multiple issues. There are limits applied to the number of issues and fields that can be edited. A single request can accommodate a maximum of 1000 issues (including subtasks) and 200 fields. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_bulk_edit_issues

`POST /rest/api/3/bulk/issues/fields` — Bulk edit issues

- Request: [[Jira v3 - Bulk edit issues]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
