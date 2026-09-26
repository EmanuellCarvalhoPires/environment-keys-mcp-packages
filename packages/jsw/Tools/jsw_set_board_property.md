---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSW]]"
tool: jsw_set_board_property
title: "JSW - Set board property"
kind: request
request: "[[JSW - Set board property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · PUT /rest/agile/1.0/board/{boardId}/properties/{propertyKey} · Set board property. Sets the value of the specified board's property. You can use this resource to store a custom data against the board identified by the id. The user who stores the data is required to have permissions to modify the board. Writes data: yes."
params:
  "boardId":
    type: string
    required: true
    description: "the ID of the board on which the property will be set."
  "propertyKey":
    type: string
    required: true
    description: "the key of the board's property. The maximum length of the key is 255 bytes."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsw_set_board_property

`PUT /rest/agile/1.0/board/{boardId}/properties/{propertyKey}` — Set board property

- Request: [[JSW - Set board property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
