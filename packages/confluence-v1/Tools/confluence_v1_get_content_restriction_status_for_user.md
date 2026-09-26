---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-restrictions
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_content_restriction_status_for_user
title: "Confluence v1 - Get content restriction status for user"
kind: request
request: "[[Confluence v1 - Get content restriction status for user]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/user · Get content restriction status for user. Returns whether the specified content restriction applies to a user. For example, if a page with id=123 has a read restriction for a user with an account ID of 384093:32b4d9w0-f6a5-3535-11a3-9c8c88d10192, the following request will return true: /wiki/rest/api/content/123/restrict… Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the content that the restriction applies to."
  "operationKey":
    type: string
    required: true
    description: "The operation that is restricted."
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
writes: false
expose: false
---
# confluence_v1_get_content_restriction_status_for_user

`GET /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/user` — Get content restriction status for user

- Request: [[Confluence v1 - Get content restriction status for user]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
