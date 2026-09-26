---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_changelogs
title: "Jira v3 - Get changelogs"
kind: request
request: "[[Jira v3 - Get changelogs]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issue/{issueIdOrKey}/changelog · Get changelogs. Returns a paginated list of all changelogs for an issue sorted by date, starting from the oldest. This operation can be accessed anonymously. Permissions required: Browse projects project permission for the project that the issue is in. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
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
# jira_get_changelogs

`GET /rest/api/3/issue/{issueIdOrKey}/changelog` — Get changelogs

- Request: [[Jira v3 - Get changelogs]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
