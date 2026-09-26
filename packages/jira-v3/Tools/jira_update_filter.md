---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/filters
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_update_filter
title: "Jira v3 - Update filter"
kind: request
request: "[[Jira v3 - Update filter]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/filter/{id} · Update filter. Updates a filter. Use this operation to update a filter's name, description, JQL, or sharing. Permissions required: Permission to access Jira, however the user must own the filter. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the filter to update."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about filter in the response. This parameter accepts a comma-separated list."
  "overrideSharePermissions":
    type: string
    required: false
    description: "EXPERIMENTAL: Whether share permissions are overridden to enable the addition of any share permissions to filters. Available to users with Administer Jira global permission."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_filter

`PUT /rest/api/3/filter/{id}` — Update filter

- Request: [[Jira v3 - Update filter]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
