---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/page
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_create_page
title: "Confluence v2 - Create page"
kind: request
request: "[[Confluence v2 - Create page]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /pages · Create page. Creates a page in the space. Pages are created as published by default unless specified as a draft in the status field. If creating a published page, the title must be specified. Permissions required: Permission to view the corresponding space. Writes data: yes."
params:
  "embedded":
    type: string
    required: false
    description: "Tag the content as embedded and content will be created in NCS."
  "private":
    type: string
    required: false
    description: "The page will be private. Only the user who creates this page will have permission to view and edit one."
  "root_level":
    type: string
    required: false
    description: "The page will be created at the root level of the space (outside the space homepage tree). If true, then a value may not be supplied for the parentId body parameter."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: true
---
# confluence_create_page

`POST /pages` — Create page

- Request: [[Confluence v2 - Create page]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
