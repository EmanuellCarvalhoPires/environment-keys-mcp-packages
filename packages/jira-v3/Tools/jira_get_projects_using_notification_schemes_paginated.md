---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-notification-schemes
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_projects_using_notification_schemes_paginated
title: "Jira v3 - Get projects using notification schemes paginated"
kind: request
request: "[[Jira v3 - Get projects using notification schemes paginated]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/notificationscheme/project · Get projects using notification schemes paginated. Returns a paginated mapping of project that have notification scheme assigned. You can provide either one or multiple notification scheme IDs or project IDs to filter by. If you don't provide any, this will return a list of all mappings. Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "notificationSchemeId":
    type: string
    required: false
    description: "The list of notifications scheme IDs to be filtered out"
  "projectId":
    type: string
    required: false
    description: "The list of project IDs to be filtered out"
writes: false
expose: false
---
# jira_get_projects_using_notification_schemes_paginated

`GET /rest/api/3/notificationscheme/project` — Get projects using notification schemes paginated

- Request: [[Jira v3 - Get projects using notification schemes paginated]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
