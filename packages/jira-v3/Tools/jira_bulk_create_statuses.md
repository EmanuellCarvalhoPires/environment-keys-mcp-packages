---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/status
  - api/operation/action
  - api/effect/write
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_bulk_create_statuses
title: "Jira v3 - Bulk create statuses"
kind: request
request: "[[Jira v3 - Bulk create statuses]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/statuses · Bulk create statuses. Creates statuses for a global or project scope. Permissions required: Administer projects project permission. Administer Jira project permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_bulk_create_statuses

`POST /rest/api/3/statuses` — Bulk create statuses

- Request: [[Jira v3 - Bulk create statuses]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
