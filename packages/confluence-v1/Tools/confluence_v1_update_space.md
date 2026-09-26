---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space
  - api/operation/update
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_update_space
title: "Confluence v1 - Update space"
kind: request
request: "[[Confluence v1 - Update space]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · PUT /wiki/rest/api/space/{spaceKey} · Update space. Updates the name, description, or homepage of a space. - For security reasons, permissions cannot be updated via the API and must be changed via the user interface instead. - Currently you cannot set space labels when updating a space. Writes data: yes."
params:
  "spaceKey":
    type: string
    required: true
    description: "The key of the space to update."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_update_space

`PUT /wiki/rest/api/space/{spaceKey}` — Update space

- Request: [[Confluence v1 - Update space]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
