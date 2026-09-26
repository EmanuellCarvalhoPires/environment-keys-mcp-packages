---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/group
  - api/operation/delete
  - api/effect/write
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_remove_member_from_group_using_group_id
title: "Confluence v1 - Remove member from group using group id"
kind: request
request: "[[Confluence v1 - Remove member from group using group id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · DELETE /wiki/rest/api/group/userByGroupId · Remove member from group using group id. Remove user as a member from a group. Permissions required: User must be a site admin. Writes data: yes."
params:
  "groupId":
    type: string
    required: true
    description: "Id of the group whose membership is updated."
  "accountId":
    type: string
    required: true
    description: "The account ID of the user. The accountId uniquely identifies the user across all Atlassian products. For example, 384093:32b4d9w0-f6a5-3535-11a3-9c8c88d10192."
  "key":
    type: string
    required: false
    description: "This parameter is no longer available and will be removed from the documentation soon. Use accountId instead. See the deprecation notice for details."
  "username":
    type: string
    required: false
    description: "This parameter is no longer available and will be removed from the documentation soon. Use accountId instead. See the deprecation notice for details."
writes: true
expose: false
---
# confluence_v1_remove_member_from_group_using_group_id

`DELETE /wiki/rest/api/group/userByGroupId` — Remove member from group using group id

- Request: [[Confluence v1 - Remove member from group using group id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
