---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-components
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_project_components_paginated
title: "Jira v3 - Get project components paginated"
kind: request
request: "[[Jira v3 - Get project components paginated]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/{projectIdOrKey}/component · Get project components paginated. Returns a paginated list of all components in a project. See the Get project components resource if you want to get a full list of versions without pagination. Writes data: no."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
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
    description: "Order the results by a field: description Sorts by the component description. issueCount Sorts by the count of issues associated with the component."
  "componentSource":
    type: string
    required: false
    description: "The source of the components to return. Can be jira (default), compass or auto. When auto is specified, the API will return connected Compass components if the project is opted into Compass, otherwise…"
  "query":
    type: string
    required: false
    description: "Filter the results using a literal string. Components with a matching name or description are returned (case insensitive)."
writes: false
expose: false
---
# jira_get_project_components_paginated

`GET /rest/api/3/project/{projectIdOrKey}/component` — Get project components paginated

- Request: [[Jira v3 - Get project components paginated]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
