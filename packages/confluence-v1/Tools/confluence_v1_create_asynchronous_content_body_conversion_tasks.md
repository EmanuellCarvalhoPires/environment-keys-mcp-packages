---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-body
  - api/operation/create
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_create_asynchronous_content_body_conversion_tasks
title: "Confluence v1 - Create asynchronous content body conversion tasks in bulk"
kind: request
request: "[[Confluence v1 - Create asynchronous content body conversion tasks in bulk]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · POST /wiki/rest/api/contentbody/convert/async/bulk/tasks · Create asynchronous content body conversion tasks in bulk. Asynchronously converts content bodies from one format to another format in bulk. Use the Content body REST API to get the status of conversion tasks. Note that there is a maximum limit of 10 conversions per request to this endpoint. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_create_asynchronous_content_body_conversion_tasks

`POST /wiki/rest/api/contentbody/convert/async/bulk/tasks` — Create asynchronous content body conversion tasks in bulk

- Request: [[Confluence v1 - Create asynchronous content body conversion tasks in bulk]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
