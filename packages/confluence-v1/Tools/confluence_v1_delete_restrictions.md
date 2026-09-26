---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-restrictions
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_delete_restrictions
title: "Confluence v1 - Delete restrictions"
kind: request
request: "[[Confluence v1 - Delete restrictions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · DELETE /wiki/rest/api/content/{id}/restriction · Delete restrictions. Removes all restrictions (read and update) on a piece of content. Permissions required: Permission to edit the content. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the content to remove restrictions from."
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the content restrictions (returned in response) to expand."
writes: true
expose: false
---
# confluence_v1_delete_restrictions

`DELETE /wiki/rest/api/content/{id}/restriction` — Delete restrictions

- Request: [[Confluence v1 - Delete restrictions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
