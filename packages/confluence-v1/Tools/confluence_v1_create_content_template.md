---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/template
  - api/operation/create
  - api/effect/write
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_create_content_template
title: "Confluence v1 - Create content template"
kind: request
request: "[[Confluence v1 - Create content template]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · POST /wiki/rest/api/template · Create content template. Creates a new content template. Note, blueprint templates cannot be created via the REST API. Permissions required: 'Admin' permission for the space to create a space template or 'Confluence Administrator' global permission to create a global template. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_create_content_template

`POST /wiki/rest/api/template` — Create content template

- Request: [[Confluence v1 - Create content template]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
