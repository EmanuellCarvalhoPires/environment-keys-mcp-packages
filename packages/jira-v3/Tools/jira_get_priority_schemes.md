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
tool: jira_get_priority_schemes
title: "Jira v3 - Get priority schemes"
kind: request
request: "[[Jira v3 - Get priority schemes]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/priorityscheme · Get priority schemes. Returns a paginated list of priority schemes. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "priorityId":
    type: string
    required: false
    description: "A set of priority IDs to filter by. To include multiple IDs, provide an ampersand-separated list. For example, priorityId=10000&priorityId=10001."
  "schemeId":
    type: string
    required: false
    description: "A set of priority scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, schemeId=10000&schemeId=10001."
  "schemeName":
    type: string
    required: false
    description: "The name of scheme to search for."
  "onlyDefault":
    type: string
    required: false
    description: "Whether only the default priority is returned."
  "orderBy":
    type: string
    required: false
    description: "The ordering to return the priority schemes by."
  "expand":
    type: string
    required: false
    description: "A comma separated list of additional information to return. \"priorities\" will return priorities associated with the priority scheme."
writes: false
expose: false
---
# jira_get_priority_schemes

`GET /rest/api/3/priorityscheme` — Get priority schemes

- Request: [[Jira v3 - Get priority schemes]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
