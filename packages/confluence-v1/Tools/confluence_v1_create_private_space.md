---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space
  - api/operation/create
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_create_private_space
title: "Confluence v1 - Create private space"
kind: request
request: "[[Confluence v1 - Create private space]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · POST /wiki/rest/api/space/_private · Create private space. Creates a new space that is only visible to the creator. This method is the same as the Create space method with permissions set to the current user only. Note, currently you cannot set space labels when creating a space. Permissions required: 'Create Space(s)' global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_create_private_space

`POST /wiki/rest/api/space/_private` — Create private space

- Request: [[Confluence v1 - Create private space]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
