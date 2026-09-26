---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-attachments
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_uri_to_download_attachment
title: "Confluence v1 - Get URI to download attachment"
kind: request
request: "[[Confluence v1 - Get URI to download attachment]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/content/{id}/child/attachment/{attachmentId}/download · Get URI to download attachment. Redirects the client to a URL that serves an attachment's binary data. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the content that the attachment is attached to."
  "attachmentId":
    type: string
    required: true
    description: "The ID of the attachment to download."
  "version":
    type: string
    required: false
    description: "The version of the attachment. If this parameter is absent, the redirect URI will download the latest version of the attachment."
  "status":
    type: string
    required: false
    description: "The statuses allowed on the retrieved attachment. If this parameter is absent, it will default to current."
writes: false
expose: false
---
# confluence_v1_get_uri_to_download_attachment

`GET /wiki/rest/api/content/{id}/child/attachment/{attachmentId}/download` — Get URI to download attachment

- Request: [[Confluence v1 - Get URI to download attachment]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
