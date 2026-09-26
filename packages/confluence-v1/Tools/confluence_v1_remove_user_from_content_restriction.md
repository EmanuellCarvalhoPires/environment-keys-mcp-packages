---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-restrictions
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_remove_user_from_content_restriction
title: "Confluence v1 - Remove user from content restriction"
kind: request
request: "[[Confluence v1 - Remove user from content restriction]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · DELETE /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/user · Remove user from content restriction. Removes a group from a content restriction. That is, remove read or update permission for the group for a piece of content. Permissions required: Permission to edit the content. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the content that the restriction applies to."
  "operationKey":
    type: string
    required: true
    description: "The operation that the restriction applies to."
  "key":
    type: string
    required: false
    description: "This parameter is no longer available and will be removed from the documentation soon. Use accountId instead. See the deprecation notice for details."
  "username":
    type: string
    required: false
    description: "This parameter is no longer available and will be removed from the documentation soon. Use accountId instead. See the deprecation notice for details."
  "accountId":
    type: string
    required: false
    description: "The account ID of the user. The accountId uniquely identifies the user across all Atlassian products. For example, 384093:32b4d9w0-f6a5-3535-11a3-9c8c88d10192."
writes: true
expose: false
---
# confluence_v1_remove_user_from_content_restriction

`DELETE /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/user` — Remove user from content restriction

- Request: [[Confluence v1 - Remove user from content restriction]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
