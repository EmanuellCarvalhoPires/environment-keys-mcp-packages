---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/objectschema
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_objectschema_attributes
title: "Assets - GET objectschema {id} attributes"
kind: request
request: "[[Assets - GET objectschema {id} attributes]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /objectschema/{id}/attributes · /objectschema/{id}/attributes. Find all object type attributes for this object schema Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
  "onlyValueEditable":
    type: string
    required: false
    description: "Return only values that are associated with values that can be edited"
  "extended":
    type: string
    required: false
    description: "Include the object type with each object type attribute"
  "query":
    type: string
    required: false
    description: "A query that will be used to filter object type attributes by their name"
writes: false
expose: false
---
# assets_get_objectschema_attributes

`GET /objectschema/{id}/attributes` — /objectschema/{id}/attributes

- Request: [[Assets - GET objectschema {id} attributes]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
