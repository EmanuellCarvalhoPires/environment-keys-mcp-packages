---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-body
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_asynchronous_content_body_conversion_task_resu
title: "Confluence v1 - Get asynchronous content body conversion task result in bulk"
kind: request
request: "[[Confluence v1 - Get asynchronous content body conversion task result in bulk]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/contentbody/convert/async/bulk/tasks · Get asynchronous content body conversion task result in bulk. Returns the content body for the corresponding asyncId of a completed conversion task. If the task is not completed, the task status is returned instead. Writes data: no."
params:
  "ids":
    type: string
    required: true
    description: "The asyncIds of the conversion tasks."
writes: false
expose: false
---
# confluence_v1_get_asynchronous_content_body_conversion_task_resu

`GET /wiki/rest/api/contentbody/convert/async/bulk/tasks` — Get asynchronous content body conversion task result in bulk

- Request: [[Confluence v1 - Get asynchronous content body conversion task result in bulk]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
