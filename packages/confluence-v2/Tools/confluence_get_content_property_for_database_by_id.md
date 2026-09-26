---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-properties
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_content_property_for_database_by_id
title: "Confluence v2 - Get content property for database by id"
kind: request
request: "[[Confluence v2 - Get content property for database by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /databases/{database-id}/properties/{property-id} · Get content property for database by id. Retrieves a specific Content Property by ID that is attached to a specified database. Permissions required: Permission to view the database. Writes data: no."
params:
  "database_id":
    type: string
    required: true
    description: "The ID of the database for which content properties should be returned."
  "property_id":
    type: string
    required: true
    description: "The ID of the content property being requested."
writes: false
expose: false
---
# confluence_get_content_property_for_database_by_id

`GET /databases/{database-id}/properties/{property-id}` — Get content property for database by id

- Request: [[Confluence v2 - Get content property for database by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
