---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_space_by_id
title: "Confluence v2 - Get space by id"
kind: request
request: "[[Confluence v2 - Get space by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /spaces/{id} · Get space by id. Returns a specific space. Permissions required: Permission to view the space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the space to be returned."
  "description_format":
    type: string
    required: false
    description: "The content format type to be returned in the description field of the response. If available, the representation will be available under a response field of the same name under the description field."
  "include_icon":
    type: string
    required: false
    description: "If the icon for the space should be fetched or not."
  "include_operations":
    type: string
    required: false
    description: "Includes operations associated with this space in the response, as defined in the Operation object. The number of results will be limited to 50 and sorted in the default sort order."
  "include_properties":
    type: string
    required: false
    description: "Includes space properties associated with this space in the response. The number of results will be limited to 50 and sorted in the default sort order."
  "include_permissions":
    type: string
    required: false
    description: "Includes space permissions associated with this space in the response. The number of results will be limited to 50 and sorted in the default sort order."
  "include_role_assignments":
    type: string
    required: false
    description: "Includes role assignments associated with this space in the response. This parameter is only accepted for EAP sites. The number of results will be limited to 50 and sorted in the default sort order."
  "include_labels":
    type: string
    required: false
    description: "Includes labels associated with this space in the response. The number of results will be limited to 50 and sorted in the default sort order."
writes: false
expose: false
---
# confluence_get_space_by_id

`GET /spaces/{id}` — Get space by id

- Request: [[Confluence v2 - Get space by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
