---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_all_workflow_schemes
title: "Jira v3 - Get all workflow schemes"
kind: request
request: "[[Jira v3 - Get all workflow schemes]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/workflowscheme · Get all workflow schemes. Returns a paginated list of all workflow schemes, not including draft workflow schemes. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
writes: false
expose: false
---
# jira_get_all_workflow_schemes

`GET /rest/api/3/workflowscheme` — Get all workflow schemes

- Request: [[Jira v3 - Get all workflow schemes]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
