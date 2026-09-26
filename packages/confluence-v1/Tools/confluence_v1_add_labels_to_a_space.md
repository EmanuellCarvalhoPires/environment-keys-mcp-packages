---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/experimental
  - api/operation/create
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_add_labels_to_a_space
title: "Confluence v1 - Add labels to a space"
kind: request
request: "[[Confluence v1 - Add labels to a space]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · POST /wiki/rest/api/space/{spaceKey}/label · Add labels to a space. Adds labels to a piece of content. Does not modify the existing labels. Notes: - Labels can also be added when creating content (Create content). - Labels can be updated when updating content (Update content). Writes data: yes."
params:
  "spaceKey":
    type: string
    required: true
    description: "The key of the space to add labels to."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_add_labels_to_a_space

`POST /wiki/rest/api/space/{spaceKey}/label` — Add labels to a space

- Request: [[Confluence v1 - Add labels to a space]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
