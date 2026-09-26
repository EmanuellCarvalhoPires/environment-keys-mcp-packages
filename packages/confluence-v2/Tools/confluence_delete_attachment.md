---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/attachment
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_delete_attachment
title: "Confluence v2 - Delete attachment"
kind: request
request: "[[Confluence v2 - Delete attachment]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · DELETE /attachments/{id} · Delete attachment. Delete an attachment by id. Deleting an attachment moves the attachment to the trash, where it can be restored later. To permanently delete an attachment (or \"purge\" it), the endpoint must be called on a trashed attachment with the following param purge=true. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the attachment to be deleted."
  "purge":
    type: string
    required: false
    description: "If attempting to purge the attachment."
writes: true
expose: false
---
# confluence_delete_attachment

`DELETE /attachments/{id}` — Delete attachment

- Request: [[Confluence v2 - Delete attachment]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
