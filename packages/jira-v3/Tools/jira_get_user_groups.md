---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/users
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_user_groups
title: "Jira v3 - Get user groups"
kind: request
request: "[[Jira v3 - Get user groups]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/user/groups · Get user groups. Returns the groups to which a user belongs. Permissions required: Browse users and groups global permission. Writes data: no."
params:
  "accountId":
    type: string
    required: true
    description: "The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, 5b10ac8d82e05b22cc7d4ef5."
  "username":
    type: string
    required: false
    description: "This parameter is no longer available. See the deprecation notice for details."
  "key":
    type: string
    required: false
    description: "This parameter is no longer available. See the deprecation notice for details."
writes: false
expose: false
---
# jira_get_user_groups

`GET /rest/api/3/user/groups` — Get user groups

- Request: [[Jira v3 - Get user groups]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
