---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/app-properties
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_deletes_a_forge_app_property
title: "Confluence v2 - Deletes a Forge app property"
kind: request
request: "[[Confluence v2 - Deletes a Forge app property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · DELETE /app/properties/{propertyKey} · Deletes a Forge app property.. Deletes a Forge app property. This API can only be accessed using asApp() requests from Forge. Writes data: yes."
params:
  "propertyKey":
    type: string
    required: true
    description: "The key of the property"
writes: true
expose: false
---
# confluence_deletes_a_forge_app_property

`DELETE /app/properties/{propertyKey}` — Deletes a Forge app property.

- Request: [[Confluence v2 - Deletes a Forge app property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
