---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-permissions
  - api/operation/create
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_add_new_permission_to_space
title: "Confluence v1 - Add new permission to space"
kind: request
request: "[[Confluence v1 - Add new permission to space]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · POST /wiki/rest/api/space/{spaceKey}/permission · Add new permission to space. Adds new permission to space. If the permission to be added is a group permission, the group can be identified by its group name or group id. Note: Apps cannot access this REST resource - including when utilizing user impersonation. Writes data: yes."
params:
  "spaceKey":
    type: string
    required: true
    description: "The key of the space to be queried for its content."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_add_new_permission_to_space

`POST /wiki/rest/api/space/{spaceKey}/permission` — Add new permission to space

- Request: [[Confluence v1 - Add new permission to space]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
