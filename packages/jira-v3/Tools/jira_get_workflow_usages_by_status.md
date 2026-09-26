---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/status
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_workflow_usages_by_status
title: "Jira v3 - Get workflow usages by status"
kind: request
request: "[[Jira v3 - Get workflow usages by status]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/statuses/{statusId}/workflowUsages · Get workflow usages by status. Returns a page of workflows using a given status. Writes data: no."
params:
  "statusId":
    type: string
    required: true
    description: "The statusId to fetch workflow usages for"
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
# jira_get_workflow_usages_by_status

`GET /rest/api/3/statuses/{statusId}/workflowUsages` — Get workflow usages by status

- Request: [[Jira v3 - Get workflow usages by status]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
