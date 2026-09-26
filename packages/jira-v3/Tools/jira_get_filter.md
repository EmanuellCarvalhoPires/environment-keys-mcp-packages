---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/filters
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_filter
title: "Jira v3 - Get filter"
kind: request
request: "[[Jira v3 - Get filter]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/filter/{id} · Get filter. Returns a filter. This operation can be accessed anonymously. Permissions required: None, however, the filter is only returned where it is: owned by the user. shared with a group that the user is a member of. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the filter to return."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about filter in the response. This parameter accepts a comma-separated list."
  "overrideSharePermissions":
    type: string
    required: false
    description: "EXPERIMENTAL: Whether share permissions are overridden to enable filters with any share permissions to be returned. Available to users with Administer Jira global permission."
writes: false
expose: false
---
# jira_get_filter

`GET /rest/api/3/filter/{id}` — Get filter

- Request: [[Jira v3 - Get filter]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
