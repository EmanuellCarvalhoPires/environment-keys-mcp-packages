---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-properties
  - api/operation/update
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_update_content_property_for_folder_by_id
title: "Confluence v2 - Update content property for folder by id"
kind: request
request: "[[Confluence v2 - Update content property for folder by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · PUT /folders/{folder-id}/properties/{property-id} · Update content property for folder by id. Update a content property for a folder by its id. Permissions required: Permission to edit the folder. Writes data: yes."
params:
  "folder_id":
    type: string
    required: true
    description: "The ID of the folder the property belongs to."
  "property_id":
    type: string
    required: true
    description: "The ID of the property to be updated."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_update_content_property_for_folder_by_id

`PUT /folders/{folder-id}/properties/{property-id}` — Update content property for folder by id

- Request: [[Confluence v2 - Update content property for folder by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
