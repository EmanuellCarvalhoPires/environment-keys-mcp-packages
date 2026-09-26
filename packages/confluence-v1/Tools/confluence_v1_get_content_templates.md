---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/template
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_content_templates
title: "Confluence v1 - Get content templates"
kind: request
request: "[[Confluence v1 - Get content templates]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/template/page · Get content templates. Returns all content templates. Use this method to retrieve all global content templates or all content templates in a space. Writes data: no."
params:
  "spaceKey":
    type: string
    required: false
    description: "The key of the space to be queried for templates. If the spaceKey is not specified, global templates will be returned."
  "start":
    type: string
    required: false
    description: "The starting index of the returned templates."
  "limit":
    type: string
    required: false
    description: "The maximum number of templates to return per page. Note, this may be restricted by fixed system limits."
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the template to expand. - body or body.storage returns the content of the template in storage format."
writes: false
expose: false
---
# confluence_v1_get_content_templates

`GET /wiki/rest/api/template/page` — Get content templates

- Request: [[Confluence v1 - Get content templates]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
