---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-body
  - api/operation/action
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_asynchronously_convert_content_body
title: "Confluence v1 - Asynchronously convert content body"
kind: request
request: "[[Confluence v1 - Asynchronously convert content body]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · POST /wiki/rest/api/contentbody/convert/async/{to} · Asynchronously convert content body. Converts a content body from one format to another format asynchronously. Returns the asyncId for the asynchronous task. Writes data: yes."
params:
  "to":
    type: string
    required: true
    description: "The name of the target format for the content body."
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the content to expand and populate. Expands are dependent on the to conversion format and may be irrelevant for certain conversions (e.g."
  "spaceKeyContext":
    type: string
    required: false
    description: "The space key used for resolving embedded content (page includes, files, and links) in the content body."
  "contentIdContext":
    type: string
    required: false
    description: "The content ID used to find the space for resolving embedded content (page includes, files, and links) in the content body."
  "allowCache":
    type: string
    required: false
    description: "Controls whether conversion results are cached and reused for identical requests. - false: Each request creates a new conversion task, even if an identical request was made previously."
  "embeddedContentRender":
    type: string
    required: false
    description: "Mode used for rendering embedded content, like attachments. - current renders the embedded content using the latest version."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_asynchronously_convert_content_body

`POST /wiki/rest/api/contentbody/convert/async/{to}` — Asynchronously convert content body

- Request: [[Confluence v1 - Asynchronously convert content body]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
