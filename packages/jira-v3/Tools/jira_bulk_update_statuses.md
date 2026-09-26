---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/status
  - api/operation/update
  - api/effect/write
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_bulk_update_statuses
title: "Jira v3 - Bulk update statuses"
kind: request
request: "[[Jira v3 - Bulk update statuses]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/statuses · Bulk update statuses. Updates statuses by ID. Permissions required: Administer projects project permission. Administer Jira project permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_bulk_update_statuses

`PUT /rest/api/3/statuses` — Bulk update statuses

- Request: [[Jira v3 - Bulk update statuses]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
