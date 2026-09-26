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
tool: confluence_v1_create_space
title: "Confluence v1 - Create space"
kind: request
request: "[[Confluence v1 - Create space]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · POST /wiki/rest/api/space · Create space. Creates a new space. Note, currently you cannot set space labels when creating a space. Permissions required: 'Create Space(s)' global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_create_space

`POST /wiki/rest/api/space` — Create space

- Request: [[Confluence v1 - Create space]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
