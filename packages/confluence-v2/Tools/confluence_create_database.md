---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/database
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_create_database
title: "Confluence v2 - Create database"
kind: request
request: "[[Confluence v2 - Create database]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /databases · Create database. Creates a database in the space. Permissions required: Permission to view the corresponding space. Permission to create a database in the space. Writes data: yes."
params:
  "private":
    type: string
    required: false
    description: "The database will be private. Only the user who creates this database will have permission to view and edit one."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_create_database

`POST /databases` — Create database

- Request: [[Confluence v2 - Create database]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
