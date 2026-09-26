---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/app-properties
  - api/operation/update
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_create_or_update_a_forge_app_property
title: "Confluence v2 - Create or update a Forge app property"
kind: request
request: "[[Confluence v2 - Create or update a Forge app property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · PUT /app/properties/{propertyKey} · Create or update a Forge app property.. Creates or updates a Forge app property. This API can only be accessed using asApp() requests from Forge. Writes data: yes."
params:
  "propertyKey":
    type: string
    required: true
    description: "The key of the property"
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_create_or_update_a_forge_app_property

`PUT /app/properties/{propertyKey}` — Create or update a Forge app property.

- Request: [[Confluence v2 - Create or update a Forge app property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
