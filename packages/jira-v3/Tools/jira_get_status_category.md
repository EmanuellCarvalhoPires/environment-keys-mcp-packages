---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-status-categories
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_status_category
title: "Jira v3 - Get status category"
kind: request
request: "[[Jira v3 - Get status category]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/statuscategory/{idOrKey} · Get status category. Returns a status category. Status categories provided a mechanism for categorizing statuses. Permissions required: Permission to access Jira. Writes data: no."
params:
  "idOrKey":
    type: string
    required: true
    description: "The ID or key of the status category."
writes: false
expose: false
---
# jira_get_status_category

`GET /rest/api/3/statuscategory/{idOrKey}` — Get status category

- Request: [[Jira v3 - Get status category]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
