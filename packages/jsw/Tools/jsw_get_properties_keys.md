---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/sprint
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_properties_keys
title: "JSW - Get properties keys"
kind: request
request: "[[JSW - Get properties keys]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/sprint/{sprintId}/properties · Get properties keys. Returns the keys of all properties for the sprint identified by the id. The user who retrieves the property keys is required to have permissions to view the sprint. Writes data: no."
params:
  "sprintId":
    type: string
    required: true
    description: "the ID of the sprint from which property keys will be returned."
writes: false
expose: false
---
# jsw_get_properties_keys

`GET /rest/agile/1.0/sprint/{sprintId}/properties` — Get properties keys

- Request: [[JSW - Get properties keys]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
