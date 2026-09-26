---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-screen-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_type_screen_schemes
title: "Jira v3 - Get issue type screen schemes"
kind: request
request: "[[Jira v3 - Get issue type screen schemes]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issuetypescreenscheme · Get issue type screen schemes. Returns a paginated list of issue type screen schemes. Only issue type screen schemes used in classic projects are returned. Permissions required: Administer Jira global permission. Writes data: no."
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
    description: "The list of issue type screen scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, id=10000&id=10001."
  "queryString":
    type: string
    required: false
    description: "String used to perform a case-insensitive partial match with issue type screen scheme name."
  "orderBy":
    type: string
    required: false
    description: "Order the results by a field: name Sorts by issue type screen scheme name. id Sorts by issue type screen scheme ID."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts projects that, for each issue type screen schemes, returns information about the projects the issue type screen sch…"
writes: false
expose: false
---
# jira_get_issue_type_screen_schemes

`GET /rest/api/3/issuetypescreenscheme` — Get issue type screen schemes

- Request: [[Jira v3 - Get issue type screen schemes]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
