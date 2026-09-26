---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/priority-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_projects_by_priority_scheme
title: "Jira v3 - Get projects by priority scheme"
kind: request
request: "[[Jira v3 - Get projects by priority scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/priorityscheme/{schemeId}/projects · Get projects by priority scheme. Returns a paginated list of projects by scheme. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "schemeId":
    type: string
    required: true
    description: "The priority scheme ID."
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "projectId":
    type: string
    required: false
    description: "The project IDs to filter by. For example, projectId=10000&projectId=10001."
  "query":
    type: string
    required: false
    description: "The string to query projects on by name."
writes: false
expose: false
---
# jira_get_projects_by_priority_scheme

`GET /rest/api/3/priorityscheme/{schemeId}/projects` — Get projects by priority scheme

- Request: [[Jira v3 - Get projects by priority scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
