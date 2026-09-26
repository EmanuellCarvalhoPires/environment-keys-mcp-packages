---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-labels
  - api/operation/create
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_add_labels_to_content
title: "Confluence v1 - Add labels to content"
kind: request
request: "[[Confluence v1 - Add labels to content]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · POST /wiki/rest/api/content/{id}/label · Add labels to content. Adds labels to a piece of content. Does not modify the existing labels. Notes: - Labels can also be added when creating content (Create content). - Labels can be updated when updating content (Update content). Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the content that will have labels added to it."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_add_labels_to_content

`POST /wiki/rest/api/content/{id}/label` — Add labels to content

- Request: [[Confluence v1 - Add labels to content]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
