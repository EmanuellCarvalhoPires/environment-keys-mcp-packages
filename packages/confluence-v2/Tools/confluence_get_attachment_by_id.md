---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/attachment
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_attachment_by_id
title: "Confluence v2 - Get attachment by id"
kind: request
request: "[[Confluence v2 - Get attachment by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /attachments/{id} · Get attachment by id. Returns a specific attachment. Permissions required: Permission to view the attachment's container. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the attachment to be returned. If you don't know the attachment's ID, use Get attachments for page/blogpost/custom content."
  "version":
    type: string
    required: false
    description: "Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details."
  "include_labels":
    type: string
    required: false
    description: "Includes labels associated with this attachment in the response. The number of results will be limited to 50 and sorted in the default sort order."
  "include_properties":
    type: string
    required: false
    description: "Includes content properties associated with this attachment in the response. The number of results will be limited to 50 and sorted in the default sort order."
  "include_operations":
    type: string
    required: false
    description: "Includes operations associated with this attachment in the response, as defined in the Operation object. The number of results will be limited to 50 and sorted in the default sort order."
  "include_versions":
    type: string
    required: false
    description: "Includes versions associated with this attachment in the response. The number of results will be limited to 50 and sorted in the default sort order."
  "include_version":
    type: string
    required: false
    description: "Includes the current version associated with this attachment in the response. By default this is included and can be omitted by setting the value to false."
  "include_collaborators":
    type: string
    required: false
    description: "Includes collaborators on the attachment."
writes: false
expose: false
---
# confluence_get_attachment_by_id

`GET /attachments/{id}` — Get attachment by id

- Request: [[Confluence v2 - Get attachment by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
