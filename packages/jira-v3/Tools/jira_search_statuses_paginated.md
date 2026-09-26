---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/status
  - api/operation/search
  - api/effect/read
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_search_statuses_paginated
title: "Jira v3 - Search statuses paginated"
kind: request
request: "[[Jira v3 - Search statuses paginated]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/statuses/search · Search statuses paginated. Returns a paginated list of statuses that match a search on name or project. Permissions required: Administer projects project permission. Administer Jira project permission. Writes data: no."
params:
  "projectId":
    type: string
    required: false
    description: "The project the status is part of or null for global statuses."
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "searchString":
    type: string
    required: false
    description: "Term to match status names against or null to search for all statuses in the search scope."
  "statusCategory":
    type: string
    required: false
    description: "Category of the status to filter by. The supported values are: TODO, INPROGRESS, and DONE."
  "includeGlobalStatuses":
    type: string
    required: false
    description: "Whether to include global statuses (scope = null, not tied to any project) in the response. Defaults to false. Only relevant for project scoped queries."
writes: false
expose: false
---
# jira_search_statuses_paginated

`GET /rest/api/3/statuses/search` — Search statuses paginated

- Request: [[Jira v3 - Search statuses paginated]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
