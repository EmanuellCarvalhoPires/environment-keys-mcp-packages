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
tool: confluence_v1_delete_user_group
title: "Confluence v1 - Delete user group"
kind: request
request: "[[Confluence v1 - Delete user group]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · DELETE /wiki/rest/api/group/by-id · Delete user group. Delete user group. Permissions required: User must be a site admin. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "Id of the group to delete."
writes: true
expose: false
---
# confluence_v1_delete_user_group

`DELETE /wiki/rest/api/group/by-id` — Delete user group

- Request: [[Confluence v1 - Delete user group]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
