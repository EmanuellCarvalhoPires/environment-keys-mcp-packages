---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/experimental
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_remove_label_from_a_space
title: "Confluence v1 - Remove label from a space"
kind: request
request: "[[Confluence v1 - Remove label from a space]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · DELETE /wiki/rest/api/space/{spaceKey}/label · Remove label from a space. Writes data: yes."
params:
  "spaceKey":
    type: string
    required: true
    description: "The key of the space to remove a labels from."
  "name":
    type: string
    required: true
    description: "The name of the label to remove"
  "prefix":
    type: string
    required: false
    description: "The prefix of the label to remove. If not provided defaults to global."
writes: true
expose: false
---
# confluence_v1_remove_label_from_a_space

`DELETE /wiki/rest/api/space/{spaceKey}/label` — Remove label from a space

- Request: [[Confluence v1 - Remove label from a space]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
