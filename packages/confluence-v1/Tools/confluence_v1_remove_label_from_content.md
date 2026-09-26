---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-labels
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_remove_label_from_content
title: "Confluence v1 - Remove label from content"
kind: request
request: "[[Confluence v1 - Remove label from content]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · DELETE /wiki/rest/api/content/{id}/label/{label} · Remove label from content. Removes a label from a piece of content. Labels can't be deleted from archived content. This is similar to Remove label from content using query parameter except that the label name is specified via a path parameter. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the content that the label will be removed from."
  "label":
    type: string
    required: true
    description: "The name of the label to be removed."
writes: true
expose: false
---
# confluence_v1_remove_label_from_content

`DELETE /wiki/rest/api/content/{id}/label/{label}` — Remove label from content

- Request: [[Confluence v1 - Remove label from content]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
