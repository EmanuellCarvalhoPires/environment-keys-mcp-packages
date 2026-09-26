---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/admin-key
  - api/operation/action
  - api/effect/write
  - api/version/v2
  - api/permission/global-admin
up: "[[MCP - Confluence v2]]"
tool: confluence_enable_admin_key
title: "Confluence v2 - Enable Admin Key"
kind: request
request: "[[Confluence v2 - Enable Admin Key]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /admin-key · Enable Admin Key. Enables admin key access for the calling user within the site. If an admin key already exists for the user, a new one will be issued with an updated expiration time. Note: The durationInMinutes field within the request body is optional. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_enable_admin_key

`POST /admin-key` — Enable Admin Key

- Request: [[Confluence v2 - Enable Admin Key]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
