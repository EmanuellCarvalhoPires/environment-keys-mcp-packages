---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/users
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_user_default_columns
title: "Jira v3 - Get user default columns"
kind: request
request: "[[Jira v3 - Get user default columns]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/user/columns · Get user default columns. Returns the default issue table columns for the user. If accountId is not passed in the request, the calling user's details are returned. Permissions required: Administer Jira global permission, to get the column details for any user. Writes data: no."
params:
  "accountId":
    type: string
    required: false
    description: "The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, 5b10ac8d82e05b22cc7d4ef5."
  "username":
    type: string
    required: false
    description: "This parameter is no longer available See the deprecation notice for details."
writes: false
expose: false
---
# jira_get_user_default_columns

`GET /rest/api/3/user/columns` — Get user default columns

- Request: [[Jira v3 - Get user default columns]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
