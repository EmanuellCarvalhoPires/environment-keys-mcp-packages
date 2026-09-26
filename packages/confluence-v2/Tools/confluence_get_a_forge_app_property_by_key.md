---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/app-properties
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_a_forge_app_property_by_key
title: "Confluence v2 - Get a Forge app property by key"
kind: request
request: "[[Confluence v2 - Get a Forge app property by key]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /app/properties/{propertyKey} · Get a Forge app property by key.. Gets a Forge app property by property key. This API can only be accessed using asApp() requests from Forge. Writes data: no."
params:
  "propertyKey":
    type: string
    required: true
    description: "The key of the property"
writes: false
expose: false
---
# confluence_get_a_forge_app_property_by_key

`GET /app/properties/{propertyKey}` — Get a Forge app property by key.

- Request: [[Confluence v2 - Get a Forge app property by key]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
