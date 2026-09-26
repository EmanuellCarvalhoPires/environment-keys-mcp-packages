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
tool: confluence_v1_create_new_user_group
title: "Confluence v1 - Create new user group"
kind: request
request: "[[Confluence v1 - Create new user group]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · POST /wiki/rest/api/group · Create new user group. Creates a new user group. Permissions required: User must be a site admin. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_create_new_user_group

`POST /wiki/rest/api/group` — Create new user group

- Request: [[Confluence v1 - Create new user group]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
