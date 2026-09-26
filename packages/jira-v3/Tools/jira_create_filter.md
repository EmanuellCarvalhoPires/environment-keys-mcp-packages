---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/filters
  - api/operation/create
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_create_filter
title: "Jira v3 - Create filter"
kind: request
request: "[[Jira v3 - Create filter]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/filter · Create filter. Creates a filter. The filter is shared according to the default share scope. The filter is not selected as a favorite. Permissions required: Permission to access Jira. Writes data: yes."
params:
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about filter in the response. This parameter accepts a comma-separated list."
  "overrideSharePermissions":
    type: string
    required: false
    description: "EXPERIMENTAL: Whether share permissions are overridden to enable filters with any share permissions to be created. Available to users with Administer Jira global permission."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_filter

`POST /rest/api/3/filter` — Create filter

- Request: [[Jira v3 - Create filter]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
