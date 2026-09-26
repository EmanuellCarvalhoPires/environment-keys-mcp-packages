---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/jql
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_field_reference_data_post
title: "Jira v3 - Get field reference data (POST)"
kind: request
request: "[[Jira v3 - Get field reference data (POST)]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/jql/autocompletedata · Get field reference data (POST). Returns reference data for JQL searches. This is a downloadable version of the documentation provided in Advanced searching - fields reference and Advanced searching - functions reference, along with a list of JQL-reserved words. Writes data: no."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_get_field_reference_data_post

`POST /rest/api/3/jql/autocompletedata` — Get field reference data (POST)

- Request: [[Jira v3 - Get field reference data (POST)]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
