---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/custom-content
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_custom_content_by_id
title: "Confluence v2 - Get custom content by id"
kind: request
request: "[[Confluence v2 - Get custom content by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /custom-content/{id} · Get custom content by id. Returns a specific piece of custom content. Permissions required: Permission to view the custom content, the container of the custom content, and the corresponding space (if different from the container). Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the custom content to be returned. If you don't know the custom content ID, use Get Custom Content by Type and filter the results."
  "body_format":
    type: string
    required: false
    description: "The content format types to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field."
  "version":
    type: string
    required: false
    description: "Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details."
  "include_labels":
    type: string
    required: false
    description: "Includes labels associated with this custom content in the response. The number of results will be limited to 50 and sorted in the default sort order."
  "include_properties":
    type: string
    required: false
    description: "Includes content properties associated with this custom content in the response. The number of results will be limited to 50 and sorted in the default sort order."
  "include_operations":
    type: string
    required: false
    description: "Includes operations associated with this custom content in the response, as defined in the Operation object. The number of results will be limited to 50 and sorted in the default sort order."
  "include_versions":
    type: string
    required: false
    description: "Includes versions associated with this custom content in the response. The number of results will be limited to 50 and sorted in the default sort order."
  "include_version":
    type: string
    required: false
    description: "Includes the current version associated with this custom content in the response. By default this is included and can be omitted by setting the value to false."
  "include_collaborators":
    type: string
    required: false
    description: "Includes collaborators on the custom content."
writes: false
expose: false
---
# confluence_get_custom_content_by_id

`GET /custom-content/{id}` — Get custom content by id

- Request: [[Confluence v2 - Get custom content by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
