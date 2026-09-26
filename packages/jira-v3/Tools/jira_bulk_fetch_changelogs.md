---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_bulk_fetch_changelogs
title: "Jira v3 - Bulk fetch changelogs"
kind: request
request: "[[Jira v3 - Bulk fetch changelogs]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/changelog/bulkfetch · Bulk fetch changelogs. Bulk fetch changelogs for multiple issues and filter by fields Returns a paginated list of all changelogs for given issues sorted by changelog date and issue IDs, starting from the oldest changelog and smallest issue ID. Writes data: no."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_bulk_fetch_changelogs

`POST /rest/api/3/changelog/bulkfetch` — Bulk fetch changelogs

- Request: [[Jira v3 - Bulk fetch changelogs]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
