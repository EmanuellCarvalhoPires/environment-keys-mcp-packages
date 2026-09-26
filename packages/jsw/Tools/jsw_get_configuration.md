---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_configuration
title: "JSW - Get configuration"
kind: request
request: "[[JSW - Get configuration]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/board/{boardId}/configuration · Get configuration. Get the board configuration. The response contains the following fields: id \\- ID of the board. name \\- Name of the board. filter \\- Reference to the filter used by the given board. location \\- Reference to the container that the board is located in. Writes data: no."
params:
  "boardId":
    type: string
    required: true
    description: "The ID of the board for which configuration is requested."
writes: false
expose: false
---
# jsw_get_configuration

`GET /rest/agile/1.0/board/{boardId}/configuration` — Get configuration

- Request: [[JSW - Get configuration]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
