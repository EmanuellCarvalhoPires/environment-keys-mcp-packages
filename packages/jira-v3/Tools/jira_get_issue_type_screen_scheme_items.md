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
tool: jira_get_issue_type_screen_scheme_items
title: "Jira v3 - Get issue type screen scheme items"
kind: request
request: "[[Jira v3 - Get issue type screen scheme items]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issuetypescreenscheme/mapping · Get issue type screen scheme items. Returns a paginated list of issue type screen scheme items. Only issue type screen schemes used in classic projects are returned. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "issueTypeScreenSchemeId":
    type: string
    required: false
    description: "The list of issue type screen scheme IDs. To include multiple issue type screen schemes, separate IDs with ampersand: issueTypeScreenSchemeId=10000&issueTypeScreenSchemeId=10001."
writes: false
expose: false
---
# jira_get_issue_type_screen_scheme_items

`GET /rest/api/3/issuetypescreenscheme/mapping` — Get issue type screen scheme items

- Request: [[Jira v3 - Get issue type screen scheme items]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
