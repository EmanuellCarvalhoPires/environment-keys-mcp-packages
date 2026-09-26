---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-search
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_search_for_issues_using_jql_enhanced_search_post
title: "Jira v3 - Search for issues using JQL enhanced search (POST)"
kind: request
request: "[[Jira v3 - Search for issues using JQL enhanced search (POST)]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/search/jql · Search for issues using JQL enhanced search (POST). Searches for issues using JQL. Recent updates might not be immediately visible in the returned search results. If you need read-after-write consistency, you can utilize the reconcileIssues parameter to ensure stronger consistency assurances. Writes data: no."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_search_for_issues_using_jql_enhanced_search_post

`POST /rest/api/3/search/jql` — Search for issues using JQL enhanced search (POST)

- Request: [[Jira v3 - Search for issues using JQL enhanced search (POST)]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
