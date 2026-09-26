---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/screen-tabs
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_bulk_screen_tabs
title: "Jira v3 - Get bulk screen tabs"
kind: request
request: "[[Jira v3 - Get bulk screen tabs]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/screens/tabs · Get bulk screen tabs. Returns the list of tabs for a bulk of screens. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "screenId":
    type: string
    required: false
    description: "The list of screen IDs. To include multiple screen IDs, provide an ampersand-separated list. For example, screenId=10000&screenId=10001."
  "tabId":
    type: string
    required: false
    description: "The list of tab IDs. To include multiple tab IDs, provide an ampersand-separated list. For example, tabId=10000&tabId=10001."
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResult":
    type: string
    required: false
    description: "The maximum number of items to return per page. The maximum number is 100,"
writes: false
expose: false
---
# jira_get_bulk_screen_tabs

`GET /rest/api/3/screens/tabs` — Get bulk screen tabs

- Request: [[Jira v3 - Get bulk screen tabs]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
