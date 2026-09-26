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
tool: confluence_v1_remove_group_from_content_restriction
title: "Confluence v1 - Remove group from content restriction"
kind: request
request: "[[Confluence v1 - Remove group from content restriction]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · DELETE /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId} · Remove group from content restriction. Removes a group from a content restriction. That is, remove read or update permission for the group for a piece of content. Permissions required: Permission to edit the content. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the content that the restriction applies to."
  "operationKey":
    type: string
    required: true
    description: "The operation that the restriction applies to."
  "groupId":
    type: string
    required: true
    description: "The id of the group to remove from the content restriction."
writes: true
expose: false
---
# confluence_v1_remove_group_from_content_restriction

`DELETE /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId}` — Remove group from content restriction

- Request: [[Confluence v1 - Remove group from content restriction]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
