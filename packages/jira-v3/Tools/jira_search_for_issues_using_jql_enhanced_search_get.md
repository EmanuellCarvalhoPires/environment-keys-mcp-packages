---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-search
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_search_for_issues_using_jql_enhanced_search_get
title: "Jira v3 - Search for issues using JQL enhanced search (GET)"
kind: request
request: "[[Jira v3 - Search for issues using JQL enhanced search (GET)]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/search/jql · Search for issues using JQL enhanced search (GET). Searches for issues using JQL. Recent updates might not be immediately visible in the returned search results. If you need read-after-write consistency, you can utilize the reconcileIssues parameter to ensure stronger consistency assurances. Writes data: no."
params:
  "jql":
    type: string
    required: false
    description: "A JQL expression. For performance reasons, this parameter requires a bounded query. A bounded query is a query with a search restriction. Example of an unbounded query: order by key desc."
  "nextPageToken":
    type: string
    required: false
    description: "The token for a page to fetch that is not the first page. The first page has a nextPageToken of null. Use the nextPageToken to fetch the next page of issues."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page. To manage page size, API may return fewer items per page where a large number of fields or properties are requested."
  "fields":
    type: string
    required: false
    description: "A list of fields to return for each issue, use it to retrieve a subset of fields. This parameter accepts a comma-separated list. Expand options include: all Returns all fields."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about issues in the response. Note that, unlike the majority of instances where expand is specified, expand is defined as a comma-delimited string of value…"
  "properties":
    type: string
    required: false
    description: "A list of up to 5 issue properties to include in the results. This parameter accepts a comma-separated list."
  "fieldsByKeys":
    type: string
    required: false
    description: "Reference fields by their key (rather than ID). The default is false."
  "failFast":
    type: string
    required: false
    description: "Fail this request early if we can't retrieve all field data."
  "reconcileIssues":
    type: string
    required: false
    description: "Strong consistency issue ids to be reconciled with search results. Accepts max 50 ids. This list of ids should be consistent with each paginated request across different pages."
  "includeArchivedProjects":
    type: string
    required: false
    description: "Whether to also return issues that belong to archived projects. Issues in archived projects are excluded by default."
writes: false
expose: true
---
# jira_search_for_issues_using_jql_enhanced_search_get

`GET /rest/api/3/search/jql` — Search for issues using JQL enhanced search (GET)

- Request: [[Jira v3 - Search for issues using JQL enhanced search (GET)]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
