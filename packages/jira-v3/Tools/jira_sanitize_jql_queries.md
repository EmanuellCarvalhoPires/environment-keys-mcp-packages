---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/jql
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_sanitize_jql_queries
title: "Jira v3 - Sanitize JQL queries"
kind: request
request: "[[Jira v3 - Sanitize JQL queries]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/jql/sanitize · Sanitize JQL queries. Sanitizes one or more JQL queries by converting readable details into IDs where a user doesn't have permission to view the entity. Writes data: no."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_sanitize_jql_queries

`POST /rest/api/3/jql/sanitize` — Sanitize JQL queries

- Request: [[Jira v3 - Sanitize JQL queries]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
