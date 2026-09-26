---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/groups
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_remove_user_from_group
title: "Jira v3 - Remove user from group"
kind: request
request: "[[Jira v3 - Remove user from group]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/group/user · Remove user from group. Removes a user from a group. Permissions required: Site administration (that is, member of the site-admin group). Writes data: yes."
params:
  "groupname":
    type: string
    required: false
    description: "As a group's name can change, use of groupId is recommended to identify a group. The name of the group. This parameter cannot be used with the groupId parameter."
  "groupId":
    type: string
    required: false
    description: "The ID of the group. This parameter cannot be used with the groupName parameter."
  "username":
    type: string
    required: false
    description: "This parameter is no longer available. See the deprecation notice for details."
  "accountId":
    type: string
    required: true
    description: "The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, 5b10ac8d82e05b22cc7d4ef5."
writes: true
expose: false
---
# jira_remove_user_from_group

`DELETE /rest/api/3/group/user` — Remove user from group

- Request: [[Jira v3 - Remove user from group]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
