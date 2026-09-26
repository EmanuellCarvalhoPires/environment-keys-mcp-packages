---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/redactions
  - api/operation/action
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_redact_content_in_a_confluence_page
title: "Confluence v2 - Redact Content in a Confluence Page"
kind: request
request: "[[Confluence v2 - Redact Content in a Confluence Page]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /pages/{id}/redact · Redact Content in a Confluence Page. Redacts sensitive content in a Confluence page by replacing specified text ranges with redaction markers. Each redaction in the response includes a unique UUID for restoration (except code block redactions). Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the page to redact content from."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_redact_content_in_a_confluence_page

`POST /pages/{id}/redact` — Redact Content in a Confluence Page

- Request: [[Confluence v2 - Redact Content in a Confluence Page]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
