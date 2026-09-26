---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/users
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_user
title: "Jira v3 - Get user"
kind: request
request: "[[Jira v3 - Get user]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/user · Get user. Returns a user. Privacy controls are applied to the response based on the user's preferences. This could mean, for example, that the user's email address is hidden. See the Profile visibility overview for more details. Writes data: no."
params:
  "accountId":
    type: string
    required: false
    description: "The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, 5b10ac8d82e05b22cc7d4ef5. Required."
  "username":
    type: string
    required: false
    description: "This parameter is no longer available. See the deprecation notice for details."
  "key":
    type: string
    required: false
    description: "This parameter is no longer available. See the deprecation notice for details."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about users in the response. This parameter accepts a comma-separated list."
writes: false
expose: false
---
# jira_get_user

`GET /rest/api/3/user` — Get user

- Request: [[Jira v3 - Get user]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
