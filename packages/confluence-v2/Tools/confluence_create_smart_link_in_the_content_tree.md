---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/smart-link
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_create_smart_link_in_the_content_tree
title: "Confluence v2 - Create Smart Link in the content tree"
kind: request
request: "[[Confluence v2 - Create Smart Link in the content tree]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /embeds · Create Smart Link in the content tree. Creates a Smart Link in the content tree in the space. Permissions required: Permission to view the corresponding space. Permission to create a Smart Link in the content tree in the space. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_create_smart_link_in_the_content_tree

`POST /embeds` — Create Smart Link in the content tree

- Request: [[Confluence v2 - Create Smart Link in the content tree]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
