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
tool: confluence_v1_get_blueprint_templates
title: "Confluence v1 - Get blueprint templates"
kind: request
request: "[[Confluence v1 - Get blueprint templates]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/template/blueprint · Get blueprint templates. Returns all templates provided by blueprints. Use this method to retrieve all global blueprint templates or all blueprint templates in a space. Note, all global blueprints are inherited by each space. Space blueprints can be customised without affecting the global blueprints. Writes data: no."
params:
  "spaceKey":
    type: string
    required: false
    description: "The key of the space to be queried for templates. If the spaceKey is not specified, global blueprint templates will be returned."
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
# confluence_v1_get_blueprint_templates

`GET /wiki/rest/api/template/blueprint` — Get blueprint templates

- Request: [[Confluence v1 - Get blueprint templates]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
