---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflows
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_list_workflow_history_entries
title: "Jira v3 - List workflow history entries"
kind: request
request: "[[Jira v3 - List workflow history entries]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/workflow/history/list · List workflow history entries. Returns a list of workflow history entries for a specified workflow id. Note: Stored workflow data expires after 60 days. Additionally, no data from before the 30th of October 2025 is available. Writes data: no."
params:
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts a comma-separated list."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_list_workflow_history_entries

`POST /rest/api/3/workflow/history/list` — List workflow history entries

- Request: [[Jira v3 - List workflow history entries]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
