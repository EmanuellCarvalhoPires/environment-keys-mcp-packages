---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-components
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_find_components_for_projects
title: "Jira v3 - Find components for projects"
kind: request
request: "[[Jira v3 - Find components for projects]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/component · Find components for projects. Returns a paginated list of all components in a project, including global (Compass) components when applicable. This operation can be accessed anonymously. Permissions required: Browse Projects project permission for the project. Writes data: no."
params:
  "projectIdsOrKeys":
    type: string
    required: false
    description: "The project IDs and/or project keys (case sensitive)."
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "orderBy":
    type: string
    required: false
    description: "Order the results by a field: description Sorts by the component description. name Sorts by component name."
  "query":
    type: string
    required: false
    description: "Filter the results using a literal string. Components with a matching name or description are returned (case insensitive)."
writes: false
expose: false
---
# jira_find_components_for_projects

`GET /rest/api/3/component` — Find components for projects

- Request: [[Jira v3 - Find components for projects]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
