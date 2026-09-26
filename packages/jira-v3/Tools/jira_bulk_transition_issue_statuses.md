---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-bulk-operations
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_bulk_transition_issue_statuses
title: "Jira v3 - Bulk transition issue statuses"
kind: request
request: "[[Jira v3 - Bulk transition issue statuses]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/bulk/issues/transition · Bulk transition issue statuses. Use this API to submit a bulk issue status transition request. You can transition multiple issues, alongside with their valid transition Ids. You can transition up to 1,000 issues in a single operation. Permissions required: Global bulk change permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_bulk_transition_issue_statuses

`POST /rest/api/3/bulk/issues/transition` — Bulk transition issue statuses

- Request: [[Jira v3 - Bulk transition issue statuses]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
