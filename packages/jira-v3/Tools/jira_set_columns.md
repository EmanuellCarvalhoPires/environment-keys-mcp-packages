---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/filters
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_set_columns
title: "Jira v3 - Set columns"
kind: request
request: "[[Jira v3 - Set columns]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/filter/{id}/columns · Set columns. Sets the columns for a filter. Only navigable fields can be set as columns. Use Get fields to get the list fields in Jira. A navigable field has navigable set to true. The parameters for this resource are expressed as HTML form data. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the filter."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_set_columns

`PUT /rest/api/3/filter/{id}/columns` — Set columns

- Request: [[Jira v3 - Set columns]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
