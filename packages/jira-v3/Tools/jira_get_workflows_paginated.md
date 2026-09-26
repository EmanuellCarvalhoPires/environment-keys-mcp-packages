---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflows
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_workflows_paginated
title: "Jira v3 - Get workflows paginated"
kind: request
request: "[[Jira v3 - Get workflows paginated]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/workflow/search · Get workflows paginated. This will be removed on June 1, 2026; use Search workflows instead. Returns a paginated list of published classic workflows. When workflow names are specified, details of those workflows are returned. Otherwise, all published classic workflows are returned. Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "workflowName":
    type: string
    required: false
    description: "The name of a workflow to return. To include multiple workflows, provide an ampersand-separated list. For example, workflowName=name1&workflowName=name2."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts a comma-separated list."
  "queryString":
    type: string
    required: false
    description: "String used to perform a case-insensitive partial match with workflow name."
  "orderBy":
    type: string
    required: false
    description: "Order the results by a field: name Sorts by workflow name. created Sorts by create time. updated Sorts by update time."
  "isActive":
    type: string
    required: false
    description: "Filters active and inactive workflows."
writes: false
expose: false
---
# jira_get_workflows_paginated

`GET /rest/api/3/workflow/search` — Get workflows paginated

- Request: [[Jira v3 - Get workflows paginated]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
