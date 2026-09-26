---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-macro-body
  - api/operation/get
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_macro_body_by_macro_id_and_convert_representat
title: "Confluence v1 - Get macro body by macro ID and convert representation Asynchronously"
kind: request
request: "[[Confluence v1 - Get macro body by macro ID and convert representation Asynchronously]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/content/{id}/history/{version}/macro/id/{macroId}/convert/async/{to} · Get macro body by macro ID and convert representation Asynchronously. Returns Async Id of the conversion task which will convert the macro into a content body of the desired format. The result will be available for 5 minutes after completion of the conversion. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID for the content that contains the macro."
  "version":
    type: string
    required: true
    description: "The version of the content that contains the macro. Specifying 0 as the version will return the macro body for the latest content version."
  "macroId":
    type: string
    required: true
    description: "The ID of the macro. For apps, this is passed to the macro by the Connect/Forge framework."
  "to":
    type: string
    required: true
    description: "The content representation to return the macro in. Currently, the following conversions are allowed: - exportview - styledview - view"
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the content to expand and populate. Expands are dependent on the to conversion format and may be irrelevant for certain conversions (e.g."
  "allowCache":
    type: string
    required: false
    description: "Controls whether conversion results are cached and reused for identical requests. - false: Each request creates a new conversion task, even if an identical request was made previously."
  "spaceKeyContext":
    type: string
    required: false
    description: "The space key used for resolving embedded content (page includes, files, and links) in the content body."
  "embeddedContentRender":
    type: string
    required: false
    description: "Mode used for rendering embedded content, like attachments. - current renders the embedded content using the latest version."
writes: false
expose: false
---
# confluence_v1_get_macro_body_by_macro_id_and_convert_representat

`GET /wiki/rest/api/content/{id}/history/{version}/macro/id/{macroId}/convert/async/{to}` — Get macro body by macro ID and convert representation Asynchronously

- Request: [[Confluence v1 - Get macro body by macro ID and convert representation Asynchronously]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
