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
tool: confluence_get_content_property_for_whiteboard_by_id
title: "Confluence v2 - Get content property for whiteboard by id"
kind: request
request: "[[Confluence v2 - Get content property for whiteboard by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /whiteboards/{whiteboard-id}/properties/{property-id} · Get content property for whiteboard by id. Retrieves a specific Content Property by ID that is attached to a specified whiteboard. Permissions required: Permission to view the whiteboard. Writes data: no."
params:
  "whiteboard_id":
    type: string
    required: true
    description: "The ID of the whiteboard for which content properties should be returned."
  "property_id":
    type: string
    required: true
    description: "The ID of the content property being requested."
writes: false
expose: false
---
# confluence_get_content_property_for_whiteboard_by_id

`GET /whiteboards/{whiteboard-id}/properties/{property-id}` — Get content property for whiteboard by id

- Request: [[Confluence v2 - Get content property for whiteboard by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
