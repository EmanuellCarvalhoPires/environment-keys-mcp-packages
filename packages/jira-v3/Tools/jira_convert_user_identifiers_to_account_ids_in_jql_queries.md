---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/jql
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_convert_user_identifiers_to_account_ids_in_jql_queries
title: "Jira v3 - Convert user identifiers to account IDs in JQL queries"
kind: request
request: "[[Jira v3 - Convert user identifiers to account IDs in JQL queries]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/jql/pdcleaner · Convert user identifiers to account IDs in JQL queries. Converts one or more JQL queries with user identifiers (username or user key) to equivalent JQL queries with account IDs. You may wish to use this operation if your system stores JQL queries and you want to make them GDPR-compliant. Writes data: no."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_convert_user_identifiers_to_account_ids_in_jql_queries

`POST /rest/api/3/jql/pdcleaner` — Convert user identifiers to account IDs in JQL queries

- Request: [[Jira v3 - Convert user identifiers to account IDs in JQL queries]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
