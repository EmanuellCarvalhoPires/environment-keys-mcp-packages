---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_board_property
title: "JSW - Get board property"
kind: request
request: "[[JSW - Get board property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/board/{boardId}/properties/{propertyKey} · Get board property. Returns the value of the property with a given key from the board identified by the provided id. The user who retrieves the property is required to have permissions to view the board. Writes data: no."
params:
  "boardId":
    type: string
    required: true
    description: "the ID of the board from which the property will be returned."
  "propertyKey":
    type: string
    required: true
    description: "the key of the property to return."
writes: false
expose: false
---
# jsw_get_board_property

`GET /rest/agile/1.0/board/{boardId}/properties/{propertyKey}` — Get board property

- Request: [[JSW - Get board property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
