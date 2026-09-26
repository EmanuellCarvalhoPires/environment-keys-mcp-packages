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
tool: jira_search_workflows
title: "Jira v3 - Search workflows"
kind: request
request: "[[Jira v3 - Search workflows]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/workflows/search · Search workflows. Returns a paginated list of global and project workflows. If workflow names are specified in the query string, details of those workflows are returned. Otherwise, all workflows are returned. Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
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
  "scope":
    type: string
    required: false
    description: "The scope of the workflow. Global for company-managed projects and Project for team-managed projects."
  "isActive":
    type: string
    required: false
    description: "Filters active and inactive workflows."
  "projectId":
    type: string
    required: false
    description: "The ID of the project to filter the workflows by. Only workflows associated with the given project are returned."
writes: false
expose: false
---
# jira_search_workflows

`GET /rest/api/3/workflows/search` — Search workflows

- Request: [[Jira v3 - Search workflows]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
