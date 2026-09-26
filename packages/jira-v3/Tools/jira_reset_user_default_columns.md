---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/users
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_reset_user_default_columns
title: "Jira v3 - Reset user default columns"
kind: request
request: "[[Jira v3 - Reset user default columns]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/user/columns · Reset user default columns. Resets the default issue table columns for the user to the system default. If accountId is not passed, the calling user's default columns are reset. Permissions required: Administer Jira global permission, to set the columns on any user. Writes data: yes."
params:
  "accountId":
    type: string
    required: false
    description: "The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, 5b10ac8d82e05b22cc7d4ef5."
  "username":
    type: string
    required: false
    description: "This parameter is no longer available. See the deprecation notice for details."
writes: true
expose: false
---
# jira_reset_user_default_columns

`DELETE /rest/api/3/user/columns` — Reset user default columns

- Request: [[Jira v3 - Reset user default columns]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
