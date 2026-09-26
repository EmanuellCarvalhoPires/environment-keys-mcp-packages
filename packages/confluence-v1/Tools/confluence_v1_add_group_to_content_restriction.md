---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-restrictions
  - api/operation/update
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_add_group_to_content_restriction
title: "Confluence v1 - Add group to content restriction"
kind: request
request: "[[Confluence v1 - Add group to content restriction]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · PUT /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId} · Add group to content restriction. Adds a group to a content restriction by Group Id. That is, grant read or update permission to the group for a piece of content. Permissions required: Permission to edit the content. Writes data: yes."
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
    description: "The groupId of the group to add to the content restriction."
writes: true
expose: false
---
# confluence_v1_add_group_to_content_restriction

`PUT /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId}` — Add group to content restriction

- Request: [[Confluence v1 - Add group to content restriction]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
