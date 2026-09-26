---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSW]]"
tool: jsw_toggle_features
title: "JSW - Toggle features"
kind: request
request: "[[JSW - Toggle features]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · PUT /rest/agile/1.0/board/{boardId}/features · Toggle features. Writes data: yes."
params:
  "boardId":
    type: string
    required: true
    description: "Value of boardId in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsw_toggle_features

`PUT /rest/agile/1.0/board/{boardId}/features` — Toggle features

- Request: [[JSW - Toggle features]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
