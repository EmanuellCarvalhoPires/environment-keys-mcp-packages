---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/sprint
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_property
title: "JSW - Get property"
kind: request
request: "[[JSW - Get property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/sprint/{sprintId}/properties/{propertyKey} · Get property. Returns the value of the property with a given key from the sprint identified by the provided id. The user who retrieves the property is required to have permissions to view the sprint. Writes data: no."
params:
  "sprintId":
    type: string
    required: true
    description: "the ID of the sprint from which the property will be returned."
  "propertyKey":
    type: string
    required: true
    description: "the key of the property to return."
writes: false
expose: false
---
# jsw_get_property

`GET /rest/agile/1.0/sprint/{sprintId}/properties/{propertyKey}` — Get property

- Request: [[JSW - Get property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
