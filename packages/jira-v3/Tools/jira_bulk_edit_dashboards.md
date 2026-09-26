---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_bulk_edit_dashboards
title: "Jira v3 - Bulk edit dashboards"
kind: request
request: "[[Jira v3 - Bulk edit dashboards]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/dashboard/bulk/edit · Bulk edit dashboards. Bulk edit dashboards. Maximum number of dashboards to be edited at the same time is 100. Permissions required: None The dashboards to be updated must be owned by the user, or the user must be an administrator. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_bulk_edit_dashboards

`PUT /rest/api/3/dashboard/bulk/edit` — Bulk edit dashboards

- Request: [[Jira v3 - Bulk edit dashboards]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
