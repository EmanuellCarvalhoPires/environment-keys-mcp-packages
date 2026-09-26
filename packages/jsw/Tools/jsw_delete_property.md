---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/sprint
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSW]]"
tool: jsw_delete_property
title: "JSW - Delete property"
kind: request
request: "[[JSW - Delete property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · DELETE /rest/agile/1.0/sprint/{sprintId}/properties/{propertyKey} · Delete property. Removes the property from the sprint identified by the id. Ths user removing the property is required to have permissions to modify the sprint. Writes data: yes."
params:
  "sprintId":
    type: string
    required: true
    description: "the ID of the sprint from which the property will be removed."
  "propertyKey":
    type: string
    required: true
    description: "the key of the property to remove."
writes: true
expose: false
---
# jsw_delete_property

`DELETE /rest/agile/1.0/sprint/{sprintId}/properties/{propertyKey}` — Delete property

- Request: [[JSW - Delete property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
