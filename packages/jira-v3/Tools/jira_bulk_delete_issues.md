---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-bulk-operations
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_bulk_delete_issues
title: "Jira v3 - Bulk delete issues"
kind: request
request: "[[Jira v3 - Bulk delete issues]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/bulk/issues/delete · Bulk delete issues. Use this API to submit a bulk delete request. You can delete up to 1,000 issues in a single operation. Permissions required: Global bulk change permission. Delete issues permission in all projects that contain the selected issues. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_bulk_delete_issues

`POST /rest/api/3/bulk/issues/delete` — Bulk delete issues

- Request: [[Jira v3 - Bulk delete issues]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
