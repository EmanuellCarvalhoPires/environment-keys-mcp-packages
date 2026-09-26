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
tool: confluence_v1_get_macro_body_by_macro_id
title: "Confluence v1 - Get macro body by macro ID"
kind: request
request: "[[Confluence v1 - Get macro body by macro ID]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/content/{id}/history/{version}/macro/id/{macroId} · Get macro body by macro ID. Returns the body of a macro in storage format, for the given macro ID. This includes information like the name of the macro, the body of the macro, and any macro parameters. This method is mainly used by Cloud apps. Writes data: no."
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
writes: false
expose: false
---
# confluence_v1_get_macro_body_by_macro_id

`GET /wiki/rest/api/content/{id}/history/{version}/macro/id/{macroId}` — Get macro body by macro ID

- Request: [[Confluence v1 - Get macro body by macro ID]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
