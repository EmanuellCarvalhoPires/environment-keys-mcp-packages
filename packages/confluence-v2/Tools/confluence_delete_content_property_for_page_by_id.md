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
tool: confluence_delete_content_property_for_page_by_id
title: "Confluence v2 - Delete content property for page by id"
kind: request
request: "[[Confluence v2 - Delete content property for page by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · DELETE /pages/{page-id}/properties/{property-id} · Delete content property for page by id. Deletes a content property for a page by its id. Permissions required: Permission to edit the page. Writes data: yes."
params:
  "page_id":
    type: string
    required: true
    description: "The ID of the page the property belongs to."
  "property_id":
    type: string
    required: true
    description: "The ID of the property to be deleted."
writes: true
expose: false
---
# confluence_delete_content_property_for_page_by_id

`DELETE /pages/{page-id}/properties/{property-id}` — Delete content property for page by id

- Request: [[Confluence v2 - Delete content property for page by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
