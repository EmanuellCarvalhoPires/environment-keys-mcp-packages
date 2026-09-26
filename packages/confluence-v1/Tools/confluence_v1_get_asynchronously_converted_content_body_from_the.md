---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-body
  - api/operation/get
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_asynchronously_converted_content_body_from_the
title: "Confluence v1 - Get asynchronously converted content body from the id or the current status of the task"
kind: request
request: "[[Confluence v1 - Get asynchronously converted content body from the id or the current status of the task]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/contentbody/convert/async/{id} · Get asynchronously converted content body from the id or the current status of the task.. Returns the content body for the corresponding asyncId of a completed conversion task. If the task is not completed, the task status is returned instead. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The asyncId of the macro task to get the converted body."
writes: false
expose: false
---
# confluence_v1_get_asynchronously_converted_content_body_from_the

`GET /wiki/rest/api/contentbody/convert/async/{id}` — Get asynchronously converted content body from the id or the current status of the task.

- Request: [[Confluence v1 - Get asynchronously converted content body from the id or the current status of the task]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
