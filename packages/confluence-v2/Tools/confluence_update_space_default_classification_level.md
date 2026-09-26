---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/classification-level
  - api/operation/update
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_update_space_default_classification_level
title: "Confluence v2 - Update space default classification level"
kind: request
request: "[[Confluence v2 - Update space default classification level]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · PUT /spaces/{id}/classification-level/default · Update space default classification level. Update the default classification level for a specific space. Permissions required: Permission to access the Confluence site ('Can use' global permission) and manage/space permission for the space. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the space for which default classification level should be updated."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_update_space_default_classification_level

`PUT /spaces/{id}/classification-level/default` — Update space default classification level

- Request: [[Confluence v2 - Update space default classification level]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
