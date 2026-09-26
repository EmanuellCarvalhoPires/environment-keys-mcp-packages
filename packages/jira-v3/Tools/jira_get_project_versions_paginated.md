---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_project_versions_paginated
title: "Jira v3 - Get project versions paginated"
kind: request
request: "[[Jira v3 - Get project versions paginated]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/{projectIdOrKey}/version · Get project versions paginated. Returns a paginated list of all versions in a project. See the Get project versions resource if you want to get a full list of versions without pagination. This operation can be accessed anonymously. Permissions required: Browse Projects project permission for the project. Writes data: no."
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
    description: "Order the results by a field: description Sorts by version description. name Sorts by version name. releaseDate Sorts by release date, starting with the oldest date."
  "query":
    type: string
    required: false
    description: "Filter the results using a literal string. Versions with matching name or description are returned (case insensitive)."
  "status":
    type: string
    required: false
    description: "A list of status values used to filter the results by version status. This parameter accepts a comma-separated list. The status values are released, unreleased, and archived."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts a comma-separated list."
writes: false
expose: false
---
# jira_get_project_versions_paginated

`GET /rest/api/3/project/{projectIdOrKey}/version` — Get project versions paginated

- Request: [[Jira v3 - Get project versions paginated]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
