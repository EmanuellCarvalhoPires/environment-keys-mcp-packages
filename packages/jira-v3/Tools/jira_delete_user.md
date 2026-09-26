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
tool: jira_delete_user
title: "Jira v3 - Delete user"
kind: request
request: "[[Jira v3 - Delete user]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/user · Delete user. Deletes a user. If the operation completes successfully then the user is removed from Jira's user base. This operation does not delete the user's Atlassian account. Permissions required: Site administration (that is, membership of the site-admin group). Writes data: yes."
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
writes: true
expose: false
---
# jira_delete_user

`DELETE /rest/api/3/user` — Delete user

- Request: [[Jira v3 - Delete user]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
