---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/attachment
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_download_attachment_thumbnail_by_id
title: "Confluence v2 - Download attachment thumbnail by id"
kind: request
request: "[[Confluence v2 - Download attachment thumbnail by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /attachments/{id}/thumbnail/download · Download attachment thumbnail by id. Redirects the client to a URL that serves an attachment thumbnail's binary data. Permissions required: Permission to view the attachment's container. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the attachment to be returned. If you don't know the attachment's ID, use Get attachments for page/blogpost/custom content."
  "version":
    type: string
    required: false
    description: "Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details."
  "height":
    type: string
    required: false
    description: "Allows you to define the thumbnail height."
  "width":
    type: string
    required: false
    description: "Allows you to define the thumbnail width."
writes: false
expose: false
---
# confluence_download_attachment_thumbnail_by_id

`GET /attachments/{id}/thumbnail/download` — Download attachment thumbnail by id

- Request: [[Confluence v2 - Download attachment thumbnail by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
