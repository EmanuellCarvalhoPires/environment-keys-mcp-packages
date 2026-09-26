---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/filters
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_favorite_filters
title: "Jira v3 - Get favorite filters"
kind: request
request: "[[Jira v3 - Get favorite filters]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/filter/favourite · Get favorite filters. Returns the visible favorite filters of the user. This operation can be accessed anonymously. Permissions required: A favorite filter is only visible to the user where the filter is: owned by the user. shared with a group that the user is a member of. Writes data: no."
params:
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about filter in the response. This parameter accepts a comma-separated list."
writes: false
expose: false
---
# jira_get_favorite_filters

`GET /rest/api/3/filter/favourite` — Get favorite filters

- Request: [[Jira v3 - Get favorite filters]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
