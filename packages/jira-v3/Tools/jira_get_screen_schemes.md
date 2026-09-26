---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/screen-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_screen_schemes
title: "Jira v3 - Get screen schemes"
kind: request
request: "[[Jira v3 - Get screen schemes]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/screenscheme · Get screen schemes. Returns a paginated list of screen schemes. Only screen schemes used in classic projects are returned. Permissions required: Administer Jira global permission. Writes data: no."
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
    description: "The list of screen scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, id=10000&id=10001."
  "expand":
    type: string
    required: false
    description: "Use expand include additional information in the response. This parameter accepts issueTypeScreenSchemes that, for each screen schemes, returns information about the issue type screen scheme the scree…"
  "queryString":
    type: string
    required: false
    description: "String used to perform a case-insensitive partial match with screen scheme name."
  "orderBy":
    type: string
    required: false
    description: "Order the results by a field: id Sorts by screen scheme ID. name Sorts by screen scheme name."
writes: false
expose: false
---
# jira_get_screen_schemes

`GET /rest/api/3/screenscheme` — Get screen schemes

- Request: [[Jira v3 - Get screen schemes]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
