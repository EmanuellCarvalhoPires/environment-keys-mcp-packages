---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSW]]"
tool: jsw_delete_board_property
title: "JSW - Delete board property"
kind: request
request: "[[JSW - Delete board property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · DELETE /rest/agile/1.0/board/{boardId}/properties/{propertyKey} · Delete board property. Removes the property from the board identified by the id. Ths user removing the property is required to have permissions to modify the board. Writes data: yes."
params:
  "boardId":
    type: string
    required: true
    description: "the id of the board from which the property will be removed."
  "propertyKey":
    type: string
    required: true
    description: "the key of the property to remove."
writes: true
expose: false
---
# jsw_delete_board_property

`DELETE /rest/agile/1.0/board/{boardId}/properties/{propertyKey}` — Delete board property

- Request: [[JSW - Delete board property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
