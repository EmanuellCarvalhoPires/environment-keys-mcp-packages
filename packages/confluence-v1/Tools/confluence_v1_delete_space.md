---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_delete_space
title: "Confluence v1 - Delete space"
kind: request
request: "[[Confluence v1 - Delete space]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · DELETE /wiki/rest/api/space/{spaceKey} · Delete space. Permanently deletes a space without sending it to the trash. Note, the space will be deleted in a long running task. Therefore, the space may not be deleted yet when this method has returned. Writes data: yes."
params:
  "spaceKey":
    type: string
    required: true
    description: "The key of the space to delete."
writes: true
expose: false
---
# confluence_v1_delete_space

`DELETE /wiki/rest/api/space/{spaceKey}` — Delete space

- Request: [[Confluence v1 - Delete space]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
