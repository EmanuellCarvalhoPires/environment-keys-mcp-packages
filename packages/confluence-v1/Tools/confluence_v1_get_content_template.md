---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/template
  - api/operation/get
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_content_template
title: "Confluence v1 - Get content template"
kind: request
request: "[[Confluence v1 - Get content template]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/template/{contentTemplateId} · Get content template. Returns a content template. This includes information about template, like the name, the space or blueprint that the template is in, the body of the template, and more. Writes data: no."
params:
  "contentTemplateId":
    type: string
    required: true
    description: "The ID of the content template to be returned."
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the template to expand. - body or body.storage returns the content of the template in storage format."
writes: false
expose: false
---
# confluence_v1_get_content_template

`GET /wiki/rest/api/template/{contentTemplateId}` — Get content template

- Request: [[Confluence v1 - Get content template]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
