---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/priority-schemes
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_suggested_priorities_for_mappings
title: "Jira v3 - Suggested priorities for mappings"
kind: request
request: "[[Jira v3 - Suggested priorities for mappings]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/priorityscheme/mappings · Suggested priorities for mappings. Returns a paginated list of priorities that would require mapping, given a change in priorities or projects associated with a priority scheme. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_suggested_priorities_for_mappings

`POST /rest/api/3/priorityscheme/mappings` — Suggested priorities for mappings

- Request: [[Jira v3 - Suggested priorities for mappings]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
