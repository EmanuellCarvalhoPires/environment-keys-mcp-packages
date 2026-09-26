---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/status
  - api/operation/delete
  - api/effect/write
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_bulk_delete_statuses
title: "Jira v3 - Bulk delete Statuses"
kind: request
request: "[[Jira v3 - Bulk delete Statuses]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/statuses · Bulk delete Statuses. Deletes statuses by ID. Permissions required: Administer projects project permission. Administer Jira project permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The list of status IDs. To include multiple IDs, provide an ampersand-separated list. For example, id=10000&id=10001. Min items 1, Max items 50"
writes: true
expose: false
---
# jira_bulk_delete_statuses

`DELETE /rest/api/3/statuses` — Bulk delete Statuses

- Request: [[Jira v3 - Bulk delete Statuses]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
