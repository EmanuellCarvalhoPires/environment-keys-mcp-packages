---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/classification-level
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_delete_space_default_classification_level
title: "Confluence v2 - Delete space default classification level"
kind: request
request: "[[Confluence v2 - Delete space default classification level]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · DELETE /spaces/{id}/classification-level/default · Delete space default classification level. Returns the default classification level for a specific space. Permissions required: Permission to access the Confluence site ('Can use' global permission) and manage/space permission for the space. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the space for which default classification level should be deleted."
writes: true
expose: false
---
# confluence_delete_space_default_classification_level

`DELETE /spaces/{id}/classification-level/default` — Delete space default classification level

- Request: [[Confluence v2 - Delete space default classification level]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
