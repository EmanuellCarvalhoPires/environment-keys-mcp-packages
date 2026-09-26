---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/sprint
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSW]]"
tool: jsw_set_property
title: "JSW - Set property"
kind: request
request: "[[JSW - Set property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · PUT /rest/agile/1.0/sprint/{sprintId}/properties/{propertyKey} · Set property. Sets the value of the specified sprint's property. You can use this resource to store a custom data against the sprint identified by the id. The user who stores the data is required to have permissions to modify the sprint. Writes data: yes."
params:
  "sprintId":
    type: string
    required: true
    description: "the ID of the sprint on which the property will be set."
  "propertyKey":
    type: string
    required: true
    description: "the key of the sprint's property. The maximum length of the key is 255 bytes."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsw_set_property

`PUT /rest/agile/1.0/sprint/{sprintId}/properties/{propertyKey}` — Set property

- Request: [[JSW - Set property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
