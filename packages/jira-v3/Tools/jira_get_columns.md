---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/filters
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_columns
title: "Jira v3 - Get columns"
kind: request
request: "[[Jira v3 - Get columns]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/filter/{id}/columns · Get columns. Returns the columns configured for a filter. The column configuration is used when the filter's results are viewed in List View with the Columns set to Filter. This operation can be accessed anonymously. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the filter."
writes: false
expose: false
---
# jira_get_columns

`GET /rest/api/3/filter/{id}/columns` — Get columns

- Request: [[Jira v3 - Get columns]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
