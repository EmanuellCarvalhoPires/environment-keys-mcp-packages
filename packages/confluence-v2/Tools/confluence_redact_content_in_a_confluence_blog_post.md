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
tool: confluence_redact_content_in_a_confluence_blog_post
title: "Confluence v2 - Redact Content in a Confluence Blog Post"
kind: request
request: "[[Confluence v2 - Redact Content in a Confluence Blog Post]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /blogposts/{id}/redact · Redact Content in a Confluence Blog Post. Redacts sensitive content in a Confluence blog post by replacing specified text ranges with redaction markers. Each redaction in the response includes a unique UUID for restoration (except code block redactions). Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the blog post to redact content from."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_redact_content_in_a_confluence_blog_post

`POST /blogposts/{id}/redact` — Redact Content in a Confluence Blog Post

- Request: [[Confluence v2 - Redact Content in a Confluence Blog Post]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
