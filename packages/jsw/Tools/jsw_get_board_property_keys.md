---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_board_property_keys
title: "JSW - Get board property keys"
kind: request
request: "[[JSW - Get board property keys]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/board/{boardId}/properties · Get board property keys. Returns the keys of all properties for the board identified by the id. The user who retrieves the property keys is required to have permissions to view the board. Writes data: no."
params:
  "boardId":
    type: string
    required: true
    description: "the ID of the board from which property keys will be returned."
writes: false
expose: false
---
# jsw_get_board_property_keys

`GET /rest/agile/1.0/board/{boardId}/properties` — Get board property keys

- Request: [[JSW - Get board property keys]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
