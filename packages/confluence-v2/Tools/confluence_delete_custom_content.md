---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/custom-content
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_delete_custom_content
title: "Confluence v2 - Delete custom content"
kind: request
request: "[[Confluence v2 - Delete custom content]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · DELETE /custom-content/{id} · Delete custom content. Delete a custom content by id. Deleting a custom content will either move it to the trash or permanently delete it (purge it), depending on the apiSupport. To permanently delete a trashed custom content, the endpoint must be called with the following param purge=true. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the custom content to be deleted."
  "purge":
    type: string
    required: false
    description: "If attempting to purge the custom content."
writes: true
expose: false
---
# confluence_delete_custom_content

`DELETE /custom-content/{id}` — Delete custom content

- Request: [[Confluence v2 - Delete custom content]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
