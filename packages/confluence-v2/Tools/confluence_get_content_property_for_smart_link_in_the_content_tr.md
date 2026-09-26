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
tool: confluence_get_content_property_for_smart_link_in_the_content_tr
title: "Confluence v2 - Get content property for Smart Link in the content tree by id"
kind: request
request: "[[Confluence v2 - Get content property for Smart Link in the content tree by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /embeds/{embed-id}/properties/{property-id} · Get content property for Smart Link in the content tree by id. Retrieves a specific Content Property by ID that is attached to a specified Smart Link in the content tree. Permissions required: Permission to view the Smart Link in the content tree. Writes data: no."
params:
  "embed_id":
    type: string
    required: true
    description: "The ID of the Smart Link in the content tree for which content properties should be returned."
  "property_id":
    type: string
    required: true
    description: "The ID of the content property being requested."
writes: false
expose: false
---
# confluence_get_content_property_for_smart_link_in_the_content_tr

`GET /embeds/{embed-id}/properties/{property-id}` — Get content property for Smart Link in the content tree by id

- Request: [[Confluence v2 - Get content property for Smart Link in the content tree by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
