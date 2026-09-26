---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/status
  - api/operation/list
  - api/effect/read
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_bulk_get_statuses
title: "Jira v3 - Bulk get statuses"
kind: request
request: "[[Jira v3 - Bulk get statuses]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/statuses · Bulk get statuses. Returns a list of the statuses specified by one or more status IDs. Permissions required: Administer projects project permission. Administer Jira project permission. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The list of status IDs. To include multiple IDs, provide an ampersand-separated list. For example, id=10000&id=10001. Min items 1, Max items 50"
writes: false
expose: false
---
# jira_bulk_get_statuses

`GET /rest/api/3/statuses` — Bulk get statuses

- Request: [[Jira v3 - Bulk get statuses]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
