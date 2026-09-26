---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_all_dashboards
title: "Jira v3 - Get all dashboards"
kind: request
request: "[[Jira v3 - Get all dashboards]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/dashboard · Get all dashboards. Returns a list of dashboards owned by or shared with the user. The list may be filtered to include only favorite or owned dashboards. This operation can be accessed anonymously. Permissions required: None. Writes data: no."
params:
  "filter":
    type: string
    required: false
    description: "The filter applied to the list of dashboards. Valid values are: favourite Returns dashboards the user has marked as favorite. my Returns dashboards owned by the user."
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
# jira_get_all_dashboards

`GET /rest/api/3/dashboard` — Get all dashboards

- Request: [[Jira v3 - Get all dashboards]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
