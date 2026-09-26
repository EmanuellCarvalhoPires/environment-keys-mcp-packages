---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/group
  - api/operation/create
  - api/effect/write
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_add_member_to_group_by_groupid
title: "Confluence v1 - Add member to group by groupId"
kind: request
request: "[[Confluence v1 - Add member to group by groupId]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · POST /wiki/rest/api/group/userByGroupId · Add member to group by groupId. Adds a user as a member in a group represented by its groupId Permissions required: User must be a site admin. Writes data: yes."
params:
  "groupId":
    type: string
    required: true
    description: "GroupId of the group whose membership is updated"
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_add_member_to_group_by_groupid

`POST /wiki/rest/api/group/userByGroupId` — Add member to group by groupId

- Request: [[Confluence v1 - Add member to group by groupId]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
