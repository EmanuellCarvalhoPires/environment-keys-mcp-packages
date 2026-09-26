---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-properties
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_delete_content_property_for_smart_link_in_the_content
title: "Confluence v2 - Delete content property for Smart Link in the content tree by id"
kind: request
request: "[[Confluence v2 - Delete content property for Smart Link in the content tree by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · DELETE /embeds/{embed-id}/properties/{property-id} · Delete content property for Smart Link in the content tree by id. Deletes a content property for a Smart Link in the content tree by its id. Permissions required: Permission to edit the Smart Link in the content tree. Writes data: yes."
params:
  "embed_id":
    type: string
    required: true
    description: "The ID of the Smart Link in the content tree the property belongs to."
  "property_id":
    type: string
    required: true
    description: "The ID of the property to be deleted."
writes: true
expose: false
---
# confluence_delete_content_property_for_smart_link_in_the_content

`DELETE /embeds/{embed-id}/properties/{property-id}` — Delete content property for Smart Link in the content tree by id

- Request: [[Confluence v2 - Delete content property for Smart Link in the content tree by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
