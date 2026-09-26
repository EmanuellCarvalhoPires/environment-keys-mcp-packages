---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflows
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_read_workflow_version_from_history
title: "Jira v3 - Read workflow version from history"
kind: request
request: "[[Jira v3 - Read workflow version from history]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/workflow/history · Read workflow version from history. Returns a workflow and related statuses for a specified workflow id and version number. Note: Stored workflow data expires after 60 days. Additionally, no data from before the 30th of October 2025 is available. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_read_workflow_version_from_history

`POST /rest/api/3/workflow/history` — Read workflow version from history

- Request: [[Jira v3 - Read workflow version from history]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
