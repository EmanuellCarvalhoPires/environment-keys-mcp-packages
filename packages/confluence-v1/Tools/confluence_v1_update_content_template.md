---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/template
  - api/operation/update
  - api/effect/write
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_update_content_template
title: "Confluence v1 - Update content template"
kind: request
request: "[[Confluence v1 - Update content template]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · PUT /wiki/rest/api/template · Update content template. Updates a content template. Note, blueprint templates cannot be updated via the REST API. Permissions required: 'Admin' permission for the space to update a space template or 'Confluence Administrator' global permission to update a global template. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_update_content_template

`PUT /wiki/rest/api/template` — Update content template

- Request: [[Confluence v1 - Update content template]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
