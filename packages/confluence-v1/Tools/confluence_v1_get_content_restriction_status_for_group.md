---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-restrictions
  - api/operation/get
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_content_restriction_status_for_group
title: "Confluence v1 - Get content restriction status for group"
kind: request
request: "[[Confluence v1 - Get content restriction status for group]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId} · Get content restriction status for group. Returns whether the specified content restriction applies to a group. For example, if a page with id=123 has a read restriction for the 123456 group id, the following request will return true: /wiki/rest/api/content/123/restriction/byOperation/read/byGroupId/123456 Note that a re… Writes data: no."
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
    description: "The id of the group to be queried for whether the content restriction applies to it."
writes: false
expose: false
---
# confluence_v1_get_content_restriction_status_for_group

`GET /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId}` — Get content restriction status for group

- Request: [[Confluence v1 - Get content restriction status for group]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
