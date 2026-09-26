---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/classification-levels
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_all_classification_levels
title: "Jira v3 - Get all classification levels"
kind: request
request: "[[Jira v3 - Get all classification levels]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/classification-levels · Get all classification levels. Returns all classification levels. Permissions required: None. Writes data: no."
params:
  "status":
    type: string
    required: false
    description: "Optional set of statuses to filter by."
  "orderBy":
    type: string
    required: false
    description: "Ordering of the results by a given field. If not provided, values will not be sorted."
writes: false
expose: false
---
# jira_get_all_classification_levels

`GET /rest/api/3/classification-levels` — Get all classification levels

- Request: [[Jira v3 - Get all classification levels]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
