---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-permissions
  - api/operation/search
  - api/effect/read
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_check_content_permissions
title: "Confluence v1 - Check content permissions"
kind: request
request: "[[Confluence v1 - Check content permissions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · POST /wiki/rest/api/content/{id}/permission/check · Check content permissions. Check if a user or a group can perform an operation to the specified content. The operation to check must be provided. The user’s account ID or the ID of the group can be provided in the subject to check permissions against a specified user or group. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the content to check permissions against."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# confluence_v1_check_content_permissions

`POST /wiki/rest/api/content/{id}/permission/check` — Check content permissions

- Request: [[Confluence v1 - Check content permissions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
