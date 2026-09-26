---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/folder
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_folder_by_id
title: "Confluence v2 - Get folder by id"
kind: request
request: "[[Confluence v2 - Get folder by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /folders/{id} · Get folder by id. Returns a specific folder. Permissions required: Permission to view the folder and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the folder to be returned."
  "include_collaborators":
    type: string
    required: false
    description: "Includes collaborators on the folder."
  "include_direct_children":
    type: string
    required: false
    description: "Includes direct children of the folder, as defined in the ChildrenResponse object."
  "include_operations":
    type: string
    required: false
    description: "Includes operations associated with this folder in the response, as defined in the Operation object. The number of results will be limited to 50 and sorted in the default sort order."
  "include_properties":
    type: string
    required: false
    description: "Includes content properties associated with this folder in the response. The number of results will be limited to 50 and sorted in the default sort order."
writes: false
expose: false
---
# confluence_get_folder_by_id

`GET /folders/{id}` — Get folder by id

- Request: [[Confluence v2 - Get folder by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
