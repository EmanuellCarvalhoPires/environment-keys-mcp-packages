---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/whiteboard
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_whiteboard_by_id
title: "Confluence v2 - Get whiteboard by id"
kind: request
request: "[[Confluence v2 - Get whiteboard by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /whiteboards/{id} · Get whiteboard by id. Returns a specific whiteboard. Permissions required: Permission to view the whiteboard and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the whiteboard to be returned"
  "include_collaborators":
    type: string
    required: false
    description: "Includes collaborators on the whiteboard."
  "include_direct_children":
    type: string
    required: false
    description: "Includes direct children of the whiteboard, as defined in the ChildrenResponse object."
  "include_operations":
    type: string
    required: false
    description: "Includes operations associated with this whiteboard in the response, as defined in the Operation object. The number of results will be limited to 50 and sorted in the default sort order."
  "include_properties":
    type: string
    required: false
    description: "Includes content properties associated with this whiteboard in the response. The number of results will be limited to 50 and sorted in the default sort order."
writes: false
expose: false
---
# confluence_get_whiteboard_by_id

`GET /whiteboards/{id}` — Get whiteboard by id

- Request: [[Confluence v2 - Get whiteboard by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
