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
tool: confluence_create_content_property_for_database
title: "Confluence v2 - Create content property for database"
kind: request
request: "[[Confluence v2 - Create content property for database]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /databases/{id}/properties · Create content property for database. Creates a new content property for a database. Permissions required: Permission to update the database. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the database to create a property for."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_create_content_property_for_database

`POST /databases/{id}/properties` — Create content property for database

- Request: [[Confluence v2 - Create content property for database]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
