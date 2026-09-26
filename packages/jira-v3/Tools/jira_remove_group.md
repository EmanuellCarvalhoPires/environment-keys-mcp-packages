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
tool: jira_remove_group
title: "Jira v3 - Remove group"
kind: request
request: "[[Jira v3 - Remove group]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/group · Remove group. Deletes a group. Permissions required: Site administration (that is, member of the site-admin strategic group). Writes data: yes."
params:
  "groupname":
    type: string
    required: false
    description: "Query parameter groupname."
  "groupId":
    type: string
    required: false
    description: "The ID of the group. This parameter cannot be used with the groupname parameter."
  "swapGroup":
    type: string
    required: false
    description: "As a group's name can change, use of swapGroupId is recommended to identify a group. The group to transfer restrictions to. Only comments and worklogs are transferred."
  "swapGroupId":
    type: string
    required: false
    description: "The ID of the group to transfer restrictions to. Only comments and worklogs are transferred. If restrictions are not transferred, comments and worklogs are inaccessible after the deletion."
writes: true
expose: false
---
# jira_remove_group

`DELETE /rest/api/3/group` — Remove group

- Request: [[Jira v3 - Remove group]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
