---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-panels
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_panel_pin_status_for_projects
title: "Jira v3 - Get issue panel pin status for projects"
kind: request
request: "[[Jira v3 - Get issue panel pin status for projects]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/forge/panel/action/bulk/status · Get issue panel pin status for projects. Get the pin status of an issue panel (added by a Forge app) for multiple projects. The operation is read-only and runs synchronously. Writes data: no."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_get_issue_panel_pin_status_for_projects

`POST /rest/api/3/forge/panel/action/bulk/status` — Get issue panel pin status for projects

- Request: [[Jira v3 - Get issue panel pin status for projects]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
