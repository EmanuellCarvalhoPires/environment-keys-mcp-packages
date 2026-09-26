---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-search
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_count_issues_using_jql
title: "Jira v3 - Count issues using JQL"
kind: request
request: "[[Jira v3 - Count issues using JQL]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/search/approximate-count · Count issues using JQL. Provide an estimated count of the issues that match the JQL. Recent updates might not be immediately visible in the returned output. This endpoint requires JQL to be bounded. This operation can be accessed anonymously. Writes data: no."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_count_issues_using_jql

`POST /rest/api/3/search/approximate-count` — Count issues using JQL

- Request: [[Jira v3 - Count issues using JQL]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
