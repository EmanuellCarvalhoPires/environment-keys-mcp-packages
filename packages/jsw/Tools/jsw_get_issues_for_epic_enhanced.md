---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/epic
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_issues_for_epic_enhanced
title: "JSW - Get issues for epic (enhanced)"
kind: request
request: "[[JSW - Get issues for epic (enhanced)]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/software/1.0/epic/{epicIdOrKey}/issue · Get issues for epic (enhanced). Returns all issues that belong to the epic, for the given epic ID. Result pagination is token based, using nextPageToken and maxResults. This only includes issues that the user has permission to view. Writes data: no."
params:
  "epicIdOrKey":
    type: string
    required: true
    description: "The ID or key of the epic that contains the requested issues."
  "nextPageToken":
    type: string
    required: false
    description: "The token for a page to fetch that is not the first page. The first page has a nextPageToken of null. Use the nextPageToken to fetch the next page of issues."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page. To manage page size, the API may return fewer items per page where there is a large number of fields or properties returned. It returns max 5000 issues."
  "reconcileIssues":
    type: string
    required: false
    description: "Strong consistency issue IDs to be reconciled with search results. Accepts max 50 IDs. This list of IDs should be consistent with each paginated request across different pages."
  "jql":
    type: string
    required: false
    description: "Filters results using a JQL query. If you define an order in your JQL query, it will override the default order of the returned issues."
  "validateQuery":
    type: string
    required: false
    description: "Specifies whether to validate the JQL query or not. Default: true."
  "fields":
    type: string
    required: false
    description: "The list of fields to return for each issue. By default, all navigable and Software project fields are returned."
  "expand":
    type: string
    required: false
    description: "A comma-separated list of the parameters to expand."
writes: false
expose: false
---
# jsw_get_issues_for_epic_enhanced

`GET /rest/software/1.0/epic/{epicIdOrKey}/issue` — Get issues for epic (enhanced)

- Request: [[JSW - Get issues for epic (enhanced)]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
