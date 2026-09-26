---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/filters
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_my_filters
title: "Jira v3 - Get my filters"
kind: request
request: "[[Jira v3 - Get my filters]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/filter/my · Get my filters. Returns the filters owned by the user. If includeFavourites is true, the user's visible favorite filters are also returned. Permissions required: Permission to access Jira, however, a favorite filters is only visible to the user where the filter is: owned by the user. Writes data: no."
params:
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about filter in the response. This parameter accepts a comma-separated list."
  "includeFavourites":
    type: string
    required: false
    description: "Include the user's favorite filters in the response."
writes: false
expose: false
---
# jira_get_my_filters

`GET /rest/api/3/filter/my` — Get my filters

- Request: [[Jira v3 - Get my filters]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
