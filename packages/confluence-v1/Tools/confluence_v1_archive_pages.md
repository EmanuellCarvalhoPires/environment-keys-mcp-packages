---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content
  - api/operation/action
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_archive_pages
title: "Confluence v1 - Archive pages"
kind: request
request: "[[Confluence v1 - Archive pages]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · POST /wiki/rest/api/content/archive · Archive pages. Archives a list of pages. The pages to be archived are specified as a list of content IDs. This API accepts the archival request and returns a task ID. The archival process happens asynchronously. Use the /longtask/ REST API to get the copy task status. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_archive_pages

`POST /wiki/rest/api/content/archive` — Archive pages

- Request: [[Confluence v1 - Archive pages]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
