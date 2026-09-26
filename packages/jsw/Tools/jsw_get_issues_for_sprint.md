---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/sprint
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_issues_for_sprint
title: "JSW - Get issues for sprint"
kind: request
request: "[[JSW - Get issues for sprint]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/sprint/{sprintId}/issue · Get issues for sprint. Returns all issues in a sprint, for a given sprint ID. This only includes issues that the user has permission to view. By default, the returned issues are ordered by rank. Writes data: no."
params:
  "sprintId":
    type: string
    required: true
    description: "The ID of the sprint that contains the requested issues."
  "startAt":
    type: string
    required: false
    description: "The starting index of the returned issues. Base index: 0. See the 'Pagination' section at the top of this page for more details."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of issues to return per page. See the 'Pagination' section at the top of this page for more details."
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
    description: "The list of fields to return for each issue. By default, all navigable and Agile fields are returned."
  "expand":
    type: string
    required: false
    description: "A comma-separated list of the parameters to expand."
writes: false
expose: true
---
# jsw_get_issues_for_sprint

`GET /rest/agile/1.0/sprint/{sprintId}/issue` — Get issues for sprint

- Request: [[JSW - Get issues for sprint]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
