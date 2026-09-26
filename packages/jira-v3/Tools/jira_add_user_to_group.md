---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/groups
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_add_user_to_group
title: "Jira v3 - Add user to group"
kind: request
request: "[[Jira v3 - Add user to group]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/group/user · Add user to group. Adds a user to a group. Permissions required: Site administration (that is, member of the site-admin group). Writes data: yes."
params:
  "groupname":
    type: string
    required: false
    description: "As a group's name can change, use of groupId is recommended to identify a group. The name of the group. This parameter cannot be used with the groupId parameter."
  "groupId":
    type: string
    required: false
    description: "The ID of the group. This parameter cannot be used with the groupName parameter."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_add_user_to_group

`POST /rest/api/3/group/user` — Add user to group

- Request: [[Jira v3 - Add user to group]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
