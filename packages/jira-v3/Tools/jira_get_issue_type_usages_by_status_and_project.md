---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/status
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_type_usages_by_status_and_project
title: "Jira v3 - Get issue type usages by status and project"
kind: request
request: "[[Jira v3 - Get issue type usages by status and project]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/statuses/{statusId}/project/{projectId}/issueTypeUsages · Get issue type usages by status and project. Returns a page of issue types in a project using a given status. Writes data: no."
params:
  "statusId":
    type: string
    required: true
    description: "The statusId to fetch issue type usages for"
  "projectId":
    type: string
    required: true
    description: "The projectId to fetch issue type usages for"
  "nextPageToken":
    type: string
    required: false
    description: "The cursor for pagination"
  "maxResults":
    type: string
    required: false
    description: "The maximum number of results to return. Must be an integer between 1 and 200."
writes: false
expose: false
---
# jira_get_issue_type_usages_by_status_and_project

`GET /rest/api/3/statuses/{statusId}/project/{projectId}/issueTypeUsages` — Get issue type usages by status and project

- Request: [[Jira v3 - Get issue type usages by status and project]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
