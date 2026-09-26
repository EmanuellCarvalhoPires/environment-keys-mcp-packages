---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/myself
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_current_user
title: "Jira v3 - Get current user"
kind: request
request: "[[Jira v3 - Get current user]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/myself · Get current user. Returns details for the current user. Permissions required: Permission to access Jira. Writes data: no."
params:
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about user in the response. This parameter accepts a comma-separated list."
writes: false
expose: true
---
# jira_get_current_user

`GET /rest/api/3/myself` — Get current user

- Request: [[Jira v3 - Get current user]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
