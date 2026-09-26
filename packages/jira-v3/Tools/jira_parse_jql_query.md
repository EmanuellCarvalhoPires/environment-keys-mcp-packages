---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/jql
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_parse_jql_query
title: "Jira v3 - Parse JQL query"
kind: request
request: "[[Jira v3 - Parse JQL query]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/jql/parse · Parse JQL query. Parses and validates JQL queries. Validation is performed in context of the current user. This operation can be accessed anonymously. Permissions required: None. Writes data: no."
params:
  "validation":
    type: string
    required: true
    description: "How to validate the JQL query and treat the validation results. Validation options include: strict Returns all errors. If validation fails, the query structure is not returned."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_parse_jql_query

`POST /rest/api/3/jql/parse` — Parse JQL query

- Request: [[Jira v3 - Parse JQL query]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
