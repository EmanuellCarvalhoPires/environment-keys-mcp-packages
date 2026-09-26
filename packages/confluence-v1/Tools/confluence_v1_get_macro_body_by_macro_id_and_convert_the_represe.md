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
tool: confluence_v1_get_macro_body_by_macro_id_and_convert_the_represe
title: "Confluence v1 - Get macro body by macro ID and convert the representation synchronously"
kind: request
request: "[[Confluence v1 - Get macro body by macro ID and convert the representation synchronously]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/content/{id}/history/{version}/macro/id/{macroId}/convert/{to} · Get macro body by macro ID and convert the representation synchronously. Returns the body of a macro in format specified in path, for the given macro ID. This includes information like the name of the macro, the body of the macro, and any macro parameters. Writes data: no."
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
    description: "The ID of the macro. This is usually passed by the app that the macro is in. Otherwise, find the macro ID by querying the desired content and version, then expanding the body in storage format."
  "to":
    type: string
    required: true
    description: "The content representation to return the macro in."
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the content to expand and populate. Expands are dependent on the to conversion format and may be irrelevant for certain conversions (e.g."
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
# confluence_v1_get_macro_body_by_macro_id_and_convert_the_represe

`GET /wiki/rest/api/content/{id}/history/{version}/macro/id/{macroId}/convert/{to}` — Get macro body by macro ID and convert the representation synchronously

- Request: [[Confluence v1 - Get macro body by macro ID and convert the representation synchronously]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
