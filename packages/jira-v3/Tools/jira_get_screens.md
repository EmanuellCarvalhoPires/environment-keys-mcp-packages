---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/screens
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_screens
title: "Jira v3 - Get screens"
kind: request
request: "[[Jira v3 - Get screens]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/screens · Get screens. Returns a paginated list of all screens or those specified by one or more screen IDs. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "id":
    type: string
    required: false
    description: "The list of screen IDs. To include multiple IDs, provide an ampersand-separated list. For example, id=10000&id=10001."
  "queryString":
    type: string
    required: false
    description: "String used to perform a case-insensitive partial match with screen name."
  "scope":
    type: string
    required: false
    description: "The scope filter string. To filter by multiple scope, provide an ampersand-separated list. For example, scope=GLOBAL&scope=PROJECT."
  "orderBy":
    type: string
    required: false
    description: "Order the results by a field: id Sorts by screen ID. name Sorts by screen name."
writes: false
expose: false
---
# jira_get_screens

`GET /rest/api/3/screens` — Get screens

- Request: [[Jira v3 - Get screens]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
