---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-search
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_check_issues_against_jql
title: "Jira v3 - Check issues against JQL"
kind: request
request: "[[Jira v3 - Check issues against JQL]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/jql/match · Check issues against JQL. Checks whether one or more issues would be returned by one or more JQL queries. Up to 10 JQL queries can be specified and up to 50 issue IDs included in the request. Writes data: no."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_check_issues_against_jql

`POST /rest/api/3/jql/match` — Check issues against JQL

- Request: [[Jira v3 - Check issues against JQL]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
