---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-panels
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_bulk_pin_or_unpin_issue_panel_to_projects
title: "Jira v3 - Bulk pin or unpin issue panel to projects"
kind: request
request: "[[Jira v3 - Bulk pin or unpin issue panel to projects]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/forge/panel/action/bulk/async · Bulk pin or unpin issue panel to projects. Bulk pin or unpin an issue panel (added by a Forge app) to or from multiple projects. The operation runs asynchronously. The response includes a task ID - use the Get task endpoint to check progress. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_bulk_pin_or_unpin_issue_panel_to_projects

`POST /rest/api/3/forge/panel/action/bulk/async` — Bulk pin or unpin issue panel to projects

- Request: [[Jira v3 - Bulk pin or unpin issue panel to projects]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
