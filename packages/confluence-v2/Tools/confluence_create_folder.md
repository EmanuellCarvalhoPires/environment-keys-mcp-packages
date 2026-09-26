---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/folder
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_create_folder
title: "Confluence v2 - Create folder"
kind: request
request: "[[Confluence v2 - Create folder]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /folders · Create folder. Creates a folder in the space. Permissions required: Permission to view the corresponding space. Permission to create a folder in the space. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_create_folder

`POST /folders` — Create folder

- Request: [[Confluence v2 - Create folder]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
