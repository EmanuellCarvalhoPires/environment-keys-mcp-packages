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
tool: jira_bulk_get_statuses_by_name
title: "Jira v3 - Bulk get statuses by name"
kind: request
request: "[[Jira v3 - Bulk get statuses by name]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/statuses/byNames · Bulk get statuses by name. Returns a list of the statuses specified by one or more status names. Permissions required: Administer projects project permission. Administer Jira project permission. Browse projects project permission. Writes data: no."
params:
  "name":
    type: string
    required: true
    description: "The list of status names. To include multiple names, provide an ampersand-separated list. For example, name=nameXX&name=nameYY. Min items 1, Max items 50"
  "projectId":
    type: string
    required: false
    description: "The project the status is part of or null for global statuses."
writes: false
expose: false
---
# jira_bulk_get_statuses_by_name

`GET /rest/api/3/statuses/byNames` — Bulk get statuses by name

- Request: [[Jira v3 - Bulk get statuses by name]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
