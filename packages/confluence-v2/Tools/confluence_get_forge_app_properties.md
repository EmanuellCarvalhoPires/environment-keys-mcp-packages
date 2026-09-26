---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/app-properties
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_forge_app_properties
title: "Confluence v2 - Get Forge app properties"
kind: request
request: "[[Confluence v2 - Get Forge app properties]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /app/properties · Get Forge app properties.. Gets Forge app properties. This API can only be accessed using asApp() requests from Forge. Writes data: no."
params:
  "cursor":
    type: string
    required: false
    description: "Used for pagination, this opaque cursor represents the last returned property key. It will be included in the response body as the next link. Use this key to request the next set of results."
  "limit":
    type: string
    required: false
    description: "Maximum number of app properties per result to return. If more results exist, use the last returned property key from the Link field in the response body as a cursor to retrieve the next set of result…"
writes: false
expose: false
---
# confluence_get_forge_app_properties

`GET /app/properties` — Get Forge app properties.

- Request: [[Confluence v2 - Get Forge app properties]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
