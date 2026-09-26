---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-properties
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_create_content_property_for_folder
title: "Confluence v2 - Create content property for folder"
kind: request
request: "[[Confluence v2 - Create content property for folder]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /folders/{id}/properties · Create content property for folder. Creates a new content property for a folder. Permissions required: Permission to update the folder. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the folder to create a property for."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_create_content_property_for_folder

`POST /folders/{id}/properties` — Create content property for folder

- Request: [[Confluence v2 - Create content property for folder]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
